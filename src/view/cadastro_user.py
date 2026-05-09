import customtkinter as ctk
from src.view.base_windows import BaseWindows
from src.controller.user_controller import ControllerUser


class CadastroUser(BaseWindows):
    def __init__(self, titulo='Cadastar - Usuário', largura=400, altura=500):
        super().__init__(titulo, largura=500, altura=600)
        self.controle = ControllerUser() # estou chamando a classe que vai controlar a incersão de dados

        self.dominio = ctk.StringVar(value='@gmail.com') # variavel que vai receber o dominio do email em menu

        # frmae onde todps os windgate sestão sendo colocados
        self.frame_principal = self.criar_frame(self,largura=450, altura=550, fg_cor=self.cores["creme"])
        self.frame_principal.place(relx=0.5, rely=0.5, anchor='center')
        
        # estou chamando o metrodo que busca as partes da tela reponsavel por abrir a tela
        self.tela_de_cadastro()



    def tela_de_cadastro(self): # metodo de executar a tela
        self.banner()
        self.field()
        self.button()

    
    def banner(self): # e reponsavel só pelo texro da tela 
        
        # frame onde a mensagem vai aparecer
        frame_mensagem = self.criar_frame(self.frame_principal, fg_cor=self.cores["marrom_escuro"], largura=500, altura=50)
        frame_mensagem.place(relx=0.5, rely=0.1, y=-40, anchor='center')

        # lebel onde a vai estar o texto
        mensagem = self.criar_label(frame_mensagem, texto='GESTÃO DE ALMOXARIFADO', tamanho_letra=22, negrito=True, cor_texto=self.cores["amarelo"])
        mensagem.place(relx=0, x=20, y=10)

    
    def field(self): # responsável por guardar os windget pra obter dados do usuario
        
        # texto nome
        nome_label = self.criar_label(self.frame_principal, texto='Nome Completo', negrito=True, cor_texto=self.cores["preto"])
        nome_label.place(relx=0, y=50)
        # entry responsavel por pegar o NOME DO USUARIO 
        self.nome_completo = self.criar_entry(self.frame_principal, placeholder='Ex: João da Silva', largura=450)
        self.nome_completo.place(relx=0, y=80)
        
        # texto email
        email_label = self.criar_label(self.frame_principal, texto='E-mail', negrito=True, cor_texto=self.cores["preto"])
        email_label.place(relx=0, y=140)
        # entry responsavel por pegar o USERNAME DO EMAIL DO USUARIO
        self.email_user = self.criar_entry(self.frame_principal, largura=200)
        self.email_user.place(relx=0, y=170)
        # munu responsavel por pegar DOMINIO DO EMAIL USUARIO
        lista=['@gmail.com', '@outlook.com', '@hotmail.com', '@yahoo.com', '@icloud.com']
        email_dominio = self.criar_menu(self.frame_principal, valores=lista, variavel=self.dominio)
        email_dominio.place(relx=0.5, y=170)
        
        # texto matricula
        matricula_label = self.criar_label(self.frame_principal, texto='Matricula', negrito=True, cor_texto=self.cores["preto"])
        matricula_label.place(relx=0, y=230)
        # entry responsavel por pegar a MATRICULA DO USUARIO
        self.matricula = self.criar_entry(self.frame_principal, placeholder='Ex: 123456789', largura=180)
        self.matricula.place(relx=0, y=260)
        
        # texto telefone
        tel_label = self.criar_label(self.frame_principal, texto='Telefone', negrito=True, cor_texto=self.cores['preto'])
        tel_label.place(relx=0.5, y=230)
        # entry responsavel por pegar o TELEFONE DO USUARIO
        self.telefone = self.criar_entry(self.frame_principal, placeholder='Ex: 00988888888', largura=180)
        self.telefone.place(relx=0.5, y=260)
        
        # texto senha
        senha_label = self.criar_label(self.frame_principal, texto='Senha', negrito=True, cor_texto=self.cores["preto"])
        senha_label.place(relx=0, y=320)
        # entry responsavel por pegar a SENHA DO USUARIO
        self.senha = self.criar_entry(self.frame_principal, largura=180)
        self.senha.place(relx=0, y=350)
        
        # texto confirmação de senha
        senhaConfirma_label = self.criar_label(self.frame_principal, texto='Confirmar Senha', negrito=True, cor_texto=self.cores["preto"])
        senhaConfirma_label.place(relx=0.5, y=320)
        # entry responsavel por pegar a CONFIRMAÇÃO DE SENHA 
        self.senha_confimacao = self.criar_entry(self.frame_principal, largura=180, senha=True)
        self.senha_confimacao.place(relx=0.5, y=350)
        
    def button(self):
        bttn_cadastrar = self.criar_botao(self.frame_principal, largura=100, espessura=40, texto="Cadastrar Usuário +", cor_texto=self.cores["preto"], fg_cor=self.cores['amarelo'], comando=self.enviar_para_controle)
        bttn_cadastrar.place(relx=0.5, y=450)
        
        bttn_cancelar = self.criar_botao(self.frame_principal, largura=150, espessura=40, fg_cor=self.cores['marrom'], texto='Cancelar',comando=self.voltar_tela_login)
        bttn_cancelar.place(relx=0, x=20, y=450)
        
        
    def voltar_tela_login(self):
        # estou importando dentro do metodo pra não ocorrer importação circular
        from src.view.login_user import LoginUser
        
        # destroy a janela cadastro
        self.destroy()
        # inicia a classe
        tl = LoginUser()
        # chamando a tela
        tl.tela_login()
        # mantém a tela aberta
        tl.mainloop()
        
        
    def enviar_para_controle(self):
        
        dados = {
            "nome": self.nome_completo.get(),
            "email": self.email_user.get(),
            "email dominio":self.dominio.get(),
            "matricula": self.matricula.get(),
            "telefone": self.telefone.get(),
            "senha": self.senha.get(),
            "senha confirma": self.senha_confimacao.get()
        }
        funcionou = self.controle.inserir_dados(dados=dados)

        if funcionou:

            self.nome_completo.delete(0, 'end')
            self.email_user.delete(0, 'end')
            self.matricula.delete(0, 'end')
            self.telefone.delete(0, 'end')
            self.senha.delete(0, 'end')
            self.senha_confimacao.delete(0, 'end')
            
        














if __name__ == "__main__":
    cda = CadastroUser()
    cda.mainloop()