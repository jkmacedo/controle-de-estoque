import customtkinter as ctk
from src.view.base_windows import BaseWindows
from src.view.cadastro_user import CadastroUser



class LoginUser(BaseWindows):
     def __init__(self, titulo='Login - Usuário', largura=400, altura=500):
          super().__init__(titulo, largura, altura)

          # criando frame master
          self.frame_principal = self.criar_frame(self)
          # posicionando frame
          self.frame_principal.place(relx=0.5, rely=0.5, anchor="center")


          # Chamando TELA DE LOGIN
          self.tela_login()
     

     def tela_login(self):
          self.banner('GESTÃO DE ALMOXARIFADO')
          self.field(texto1="Matricula", texto2="Senha")
          self.buttons()


     def banner(self, texto):
          # linha
          linha_1 = ctk.CTkFrame(self.frame_principal, fg_color=self.cores["amarelo"], width=350, height=2)
          linha_1.place(relx=0.5, rely=0, anchor="center", y=35)

          # nome
          nome = self.criar_label(self.frame_principal, tamanho_letra=25, texto=texto, negrito=True, cor_texto=self.cores["creme"])
          nome.place(relx=0.5, rely=0, anchor="center", y=60)

          # linha
          linha_1 = ctk.CTkFrame(self.frame_principal, fg_color=self.cores["amarelo"], width=350, height=2)
          linha_1.place(relx=0.5, rely=0, anchor="center", y=80)

     
     def field(self, texto1, texto2):
          # TEXTO matricula
          texto_1 = self.criar_label(self.frame_principal, texto=texto1, tamanho_letra=14, negrito=True, cor_texto=self.cores["branco"])
          texto_1.place(relx=0, rely=0.5, anchor="nw", x=55, y=-125)

          # RECEBE valor da MATRICULA --------------------------------------------------------------------------------
          self.matricula_login = self.criar_entry(self.frame_principal, placeholder=f"Digite {texto1} aqui", espessura=50)
          self.matricula_login.place(relx=0.5, rely=0, anchor="n", y=150)

          # TEXTO senha
          texto_2 = self.criar_label(self.frame_principal, texto=texto2, tamanho_letra=14, negrito=True, cor_texto=self.cores["branco"])
          texto_2.place(relx=0, rely=0.5, anchor="nw", x=55, y=-35)


          # RECEBE valor da SENHA -----------------------------------------------------------------------------------
          self.senha_login = self.criar_entry(self.frame_principal, placeholder=f"Digite sua {texto2} aqui", espessura=50, senha=True)
          self.senha_login.place(relx=0.5, rely=0, anchor="n", y=240)


     def buttons(self):
          
          # butão de verificação de login ENTRAR
          bttn = self.criar_botao(self.frame_principal, texto="ENTRAR", espessura=45, fg_cor=self.cores["amarelo"], hover_cor=self.cores["marrom"], comando= lambda: print('ENTRAR... TESTANDO...'))
          bttn.place(relx=0.5, rely=1, anchor="center", y=-145)

          # cria link para abrir a janela de CADASTRO
          bttn_link = self.criar_label(self.frame_principal, texto='Não tem cadastro? Casdastre-se aqui', front='underline', cor_texto=self.cores["azul"], mao=True)
          bttn_link.place(relx=0.5, rely=1, anchor='center', y=-80)

          # comando do link
          bttn_link.bind("<Button-1>", lambda e:self.aparecer_tela_cadastro())


     def aparecer_tela_cadastro(self):
          # escomfe o freme principal da tela de login
          self.frame_principal.place_forget()
          # estâcia
          cdt = CadastroUser()
          # chama a tela de cadastro
          cdt.tela_de_cadastro()















if __name__ == "__main__":

    lu = LoginUser()
    lu.mainloop()
