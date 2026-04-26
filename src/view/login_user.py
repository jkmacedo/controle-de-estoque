import customtkinter as ctk
from src.view.base_windows import BaseWindows


class LoginUser(BaseWindows):
     def __init__(self):
          super().__init__(titulo="Login - Usuário")

          # criando frame master
          self.frame_principal = ctk.CTkFrame(
               self,
               fg_color=self.cores["marrom_escuro"],
               corner_radius=1,
               width=400,
               height=500
          )
          # posicionando frame
          self.frame_principal.place(relx=0.5, rely=0.5, anchor="center")

          # Chamando BANNER
          self.banner()

          # chamando FIELD
          self.field()


     def banner(self):
          # linha
          linha_1 = ctk.CTkFrame(self.frame_principal, fg_color=self.cores["amarelo"], width=350, height=2)
          linha_1.place(relx=0.5, rely=0, anchor="center", y=25)

          # nome
          nome = self.criar_label(self.frame_principal, tamanho_letra=25, texto='GESTÃO DE ALMOXARIFADO', negrito=True, cor_texto="amarelo")
          nome.place(relx=0.5, rely=0, anchor="center", y=40)

          # linha
          linha_1 = ctk.CTkFrame(self.frame_principal, fg_color=self.cores["amarelo"], width=350, height=2)
          linha_1.place(relx=0.5, rely=0, anchor="center", y=55)

     
     def field(self):
          pass















if __name__ == "__main__":

    lu = LoginUser()
    lu.mainloop()
