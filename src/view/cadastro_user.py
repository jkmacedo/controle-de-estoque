import customtkinter as ctk
from src.view.base_windows import BaseWindows


class CadastroUser(BaseWindows):
    def __init__(self, titulo='Cadastar - Usuário', largura=400, altura=500):
        super().__init__(titulo, largura=500, altura=600)



    def tela_de_cadastro(self):
        print('Tá funcionando inda graças a Deus!!!!!!!!!')










if __name__ == "__main__":
    cda = CadastroUser()
    cda.mainloop()