from src.repository.user_repository import RepositoryUser
from src.view.base_windows import BaseWindows

class ControllerUser:
    def __init__(self):
        self.repo = RepositoryUser()
        self.bw = BaseWindows()
    

    def validar_dados(self, dados):

        if not all(dados.values()):
            self.bw.msgbox_incorreto(mensagem='Você deve preencher matricula e senha!')
        else:
            resultado_busca = self.repo.buscar_dados(matricula=dados["matricula"], senha=dados["senha"])

            if resultado_busca:

                matricula = self.tratar_strig(resultado_busca[0])
                senha = self.tratar_strig(resultado_busca[1])

                if self.tamanho_is_numero(matricula):

                    if matricula == dados["matricula"] and senha == dados["senha"]:
                        self.bw.msgbox_correto(mensagem='Sucesso na validação! Bem-vindo')
                        return True
                    
                else:
                    self.bw.msgbox_incorreto(mensagem='A matricula deve ter 9 carcteris e todos números')
            else:
                self.bw.msgbox_incorreto(mensagem='Usuário não encontrado')

    
    @staticmethod
    def tamanho_is_numero(matricula):

        if len(matricula) == 9 and matricula.strip().isnumeric():
            return True
        else:
            return False


    @staticmethod
    def tratar_strig(valor):
        return str(valor).strip()






if __name__ == "__main__":
    pass