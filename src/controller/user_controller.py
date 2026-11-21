from tkinter import messagebox
from src.repository.user_repository import RepositoryUser
from src.view.base_windows import BaseWindows
from src.models.user_model import Usuario
from src.security.senha import gerar_hash, senha_confere, TAMANHO_MAXIMO_BYTES

class ControllerUser:
    def __init__(self):
        self.repo = RepositoryUser()
        self.bw = BaseWindows()
        
    
    # usei no login para validar os dados
    def validar_dados(self, dados):
        # verifica se todos os valores de dados estão preechidos
        if not all(dados.values()):
            self.bw.msgbox_incorreto(mensagem='Você deve preencher matricula e senha!') #chamando o pop-up
        else:

            # busca o usuário só pela matrícula (a senha não vai mais pro SQL, o banco guarda apenas o hash dela)
            resultado_busca = self.repo.buscar_dados(matricula=dados["matricula"])
            if resultado_busca: # se tem dados no banco
                # o banco guarda a matrícula como int e perde os zeros à esquerda, então completa de novo até 9 dígitos
                matricula = self.tratar_strig(resultado_busca[0]).zfill(9)
                hash_salvo = self.tratar_strig(resultado_busca[1]) # o que está no banco é o hash, não a senha

                if self.tamanho_is_numero(matricula):
                    # confere a matrícula e pergunta ao bcrypt se a senha digitada gera aquele hash
                    if matricula == dados["matricula"] and senha_confere(dados["senha"], hash_salvo):
                        self.bw.msgbox_correto(mensagem='Sucesso na validação! Bem-vindo') # chamando pop-up
                        # devolve o id do usuário (sempre maior que 0, então continua valendo como "deu certo") pra tela saber quem logou
                        return resultado_busca[2]
                    else:
                        # mesma mensagem pra matrícula inexistente e senha errada, pra não revelar qual dos dois falhou
                        self.bw.msgbox_incorreto(mensagem='Matrícula ou senha incorreta') # chamando pop-up
                else:
                    self.bw.msgbox_incorreto(mensagem='A matricula deve ter 9 carcteris e todos números') #chamando pop-up

            else:
                self.bw.msgbox_incorreto(mensagem='Matrícula ou senha incorreta') # chamando pop-up
                
                
                
                
    def inserir_dados(self, dados):

        dados_verificados = self.verificar_dados_cadastro(dados=dados)

        # se por algum moitvo não reornar nada
        if not dados_verificados:
            return
        
        # definido antes do try pra poder usar no except mesmo se der erro cedo
        eml = str(dados_verificados["email"])

        try:

            mat = int(dados_verificados["matricula"])
            # a senha nunca vai pro banco como foi digitada: salva só o hash dela
            sen = gerar_hash(str(dados_verificados["senha"]))
            nom = str(dados_verificados["nome"])
            tel = str(dados_verificados["telefone"])

            # passoados os dados para um objeto
            user = Usuario(matricula=mat, senha=sen, nome=nom, email=eml, telefone=tel)

            # cadastrei no banco
            # o repositório devolve False se não conseguiu salvar, então não mostra "Cadastrado!" à toa
            if not self.repo.cadastrar_usuario(objeto=user):
                self.bw.msgbox_incorreto(mensagem='Não foi possivel salvar por motivos técnicos') # pop-up
                return

            self.bw.msgbox_correto(mensagem='Usuário Cadastrado!') # pop-up

            return True

        except Exception as erro:
            # obs: como as vezes da erro ao carregar a imagem do mensagebox do custamtkinter, adcionei uma verificação pra ver se o cadastro ocorreu e usei o tkinter pra evitar o erro;
            if self.repo.existe_no_banco('email', eml): 
                messagebox.showinfo('Aviso do Sistema', 'Usuário Cadastrado!')
                return True # o cadastro foi salvo, só o pop-up do CTkMessagebox que falhou
            else:
                self.bw.msgbox_incorreto(mensagem='Não foi possivel salvar por motivos técnicos') # pop-up

        




    def verificar_dados_cadastro(self, dados:dict):

        dados_dict = dados
        dados_corretos = dict() 

        # 1. Verificação de campos vazios
        for campo, valor in dados_dict.items():
            if not str(valor).strip():
                self.bw.msgbox_incorreto(mensagem='TODOS os campos devem ser preenchidos!') # pop-up
                return

        # --- NOME ---
        # Verifica se cada pedaço do nome contém apenas letras
        nome_limpo = dados_dict["nome"].strip()
        if all(pedaco.isalpha() for pedaco in nome_limpo.split()):
            dados_corretos["nome"] = nome_limpo.title()
        else:
            self.bw.msgbox_incorreto(mensagem='Seu nome não deve ter acentos, caracteres especiais ou números') # pop-up
            return

        # --- EMAIL ---
        # Verifica se a parte do usuário é alfanumérica
        usuario_email = str(dados_dict["email"]).strip()
        if usuario_email.isalnum():
            email_completo = usuario_email + dados_dict["email dominio"]
            
            # Se qtd for 0, o email está disponível
            if not self.repo.existe_no_banco(coluna="email", valor=email_completo):
                dados_corretos["email"] = email_completo
            else:
                self.bw.msgbox_incorreto(mensagem='E-mail já cadastrado') # pop-up
                return
        else:
            self.bw.msgbox_incorreto(mensagem='Coloque apenas letras e números no e-mail (antes do domínio)') # pop-up
            return

        # --- MATRÍCULA ---
        matricula = str(dados_dict["matricula"]).strip()
        if matricula.isnumeric() and len(matricula) == 9:
            if not self.repo.existe_no_banco('matricula', matricula):
                dados_corretos["matricula"] = matricula
            else:
                self.bw.msgbox_incorreto(mensagem='Matrícula já cadastrada') # pop-up
                return
        else:
            self.bw.msgbox_incorreto(mensagem='A matrícula deve ter exatamente 9 dígitos numéricos') # pop-up
            return

        # --- TELEFONE ---
        telefone = str(dados_dict["telefone"]).strip()
        if telefone.isnumeric() and len(telefone) == 11:
            # o telefone é salvo formatado, então a busca por duplicado também precisa usar o formato salvo
            telefone_formatado = self.formatar_telefone(telefone)
            if not self.repo.existe_no_banco('telefone', telefone_formatado):
                dados_corretos["telefone"] = telefone_formatado
            else:
                self.bw.msgbox_incorreto(mensagem='Telefone já cadastrado') # pop-up
                return
        else:
            self.bw.msgbox_incorreto(mensagem='Digite 11 números (DDD + Número) sem espaços ou traços') # pop-up
            return

        # --- SENHA ---
        senha = str(dados_dict["senha"]).strip()
        confirma_senha = str(dados_dict["senha confirma"]).strip()

        # Verifica se tem no mínimo 8 caracteres, se cabe no limite do bcrypt (72 bytes) e se não há espaços na string original
        if len(senha) >= 8 and len(senha.encode("utf-8")) <= TAMANHO_MAXIMO_BYTES and ' ' not in dados_dict["senha"]:
            if senha == confirma_senha:
                dados_corretos["senha"] = senha
            else:
                self.bw.msgbox_incorreto(mensagem='As senhas devem ser iguais') # pop-up
                return
        else:
            self.bw.msgbox_incorreto(mensagem='A senha deve ter de 8 a 72 caracteres e não pode conter espaços') # pop-up
            return


        # deu tudo certo e ta retornado o dicionario com os varelores para inserir
        return dados_corretos








        

        




        

    








    @staticmethod
    def tamanho_is_numero(matricula):

        if len(matricula) == 9 and matricula.strip().isnumeric():
            return True
        else:
            return False


    @staticmethod
    def tratar_strig(valor):
        return str(valor).strip()
    
    @staticmethod
    def formatar_telefone(tel):
        return f'({tel[:2]}) {tel[2:7]}-{tel[7:]}'






if __name__ == "__main__":
    pass