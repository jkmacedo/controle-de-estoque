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

          # chamando BUTTONS
          self.buttons()


     def banner(self):
          # linha
          linha_1 = ctk.CTkFrame(self.frame_principal, fg_color=self.cores["amarelo"], width=350, height=2)
          linha_1.place(relx=0.5, rely=0, anchor="center", y=35)

          # nome
          nome = self.criar_label(self.frame_principal, tamanho_letra=25, texto='GESTÃO DE ALMOXARIFADO', negrito=True, cor_texto="creme")
          nome.place(relx=0.5, rely=0, anchor="center", y=60)

          # linha
          linha_1 = ctk.CTkFrame(self.frame_principal, fg_color=self.cores["amarelo"], width=350, height=2)
          linha_1.place(relx=0.5, rely=0, anchor="center", y=80)

     
     def field(self):
          # TEXTO matricula
          texto_1 = self.criar_label(self.frame_principal, texto="Matricula", tamanho_letra=14, negrito=True, cor_texto="branco")
          texto_1.place(relx=0, rely=0.5, anchor="nw", x=55, y=-125)

          # RECEBE valor da MATRICULA --------------------------------------------------------------------------------
          self.matricula_login = self.criar_entry(self.frame_principal, placeholder="Digite sua matrícula aqui", espessura=50)
          self.matricula_login.place(relx=0.5, rely=0, anchor="n", y=150)

          # TEXTO senha
          texto_2 = self.criar_label(self.frame_principal, texto="Senha", tamanho_letra=14, negrito=True, cor_texto="branco")
          texto_2.place(relx=0, rely=0.5, anchor="nw", x=55, y=-35)


          # RECEBE valor da SENHA -----------------------------------------------------------------------------------
          self.senha_login = self.criar_entry(self.frame_principal, placeholder="Digite sua senha aqui", espessura=50, senha=True)
          self.senha_login.place(relx=0.5, rely=0, anchor="n", y=240)


     def buttons(self):
          
          # butão de verificação de login ENTRAR
          bttn = self.criar_botao(self.frame_principal, texto="ENTRAR", espessura=45, fg_cor="amarelo", hover_cor="marrom", comando= lambda: print('TESTANDO...'))
          bttn.place(relx=0.5, rely=1, anchor="center", y=-145)

          # cria link para abrir a janela de CADASTRO
          bttn_link = self.criar_label(self.frame_principal, texto='Não tem cadastro? Casdastre-se aqui', front='underline', cor_texto="azul", mao=True)
          bttn_link.place(relx=0.5, rely=1, anchor='center', y=-80)
          bttn_link.bind("<Button-1>", lambda e: print("TESTANDO..."))















if __name__ == "__main__":

    lu = LoginUser()
    lu.mainloop()
