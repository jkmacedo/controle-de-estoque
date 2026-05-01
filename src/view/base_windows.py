import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class BaseWindows(ctk.CTk):
    # Definir método construtor
    def __init__(self, titulo='nome da janela', largura=400, altura=500):
        # Herda atributos da classe pai (Ctk)
        super().__init__()


        # cria a paleta de cores do projeto
        self.cores = {
            "marrom": "#63493C",
            "marrom_escuro": "#4A362D",
            "creme": "#F4D0A1",
            "amarelo": "#FFB800",
            "preto": "#000000",
            "branco": "#FFFFFF",
            "azul": "#03A2F1",
            "vermelho":"#DC0E0E"
        }

        self.title(titulo) # titulo
        self.geometry(f'{largura}x{altura}') # define o tamanho da janela
        self.configure(fg_color=self.cores["creme"]) # define a cor de fundo da janela
        self.resizable(False, False) # não deixar o usuario esticar nem pra cima ou pra baixo

        # definir configurações para os itens na janela se adaptarem ao tamanho da janela
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


    # função para criar frame
    def criar_frame(self, master, fg_cor=False, largura=400, altura=500):
        
        return ctk.CTkFrame(
               self,
               fg_color=fg_cor if fg_cor else self.cores["marrom_escuro"],
               corner_radius=1,
               width=largura,
               height=altura
          )


    # Função para criar texto;
    def criar_label(self, master, texto, front='normal', tamanho_letra=16, negrito=False, mao=False, cor_texto=False):

        # retorna um label (texto)
        return ctk.CTkLabel(
            master,
            text=texto,
            font= ("Roboto", tamanho_letra, "bold" if negrito else front),
            text_color= cor_texto if cor_texto else self.cores["creme"],
            cursor= 'hand2' if mao else 'arrow'

        )


    # cria a barra de digitar
    def criar_entry(self, master, placeholder, largura=300, espessura=40, senha=False):

        # retorna o Entry (barra)
        return ctk.CTkEntry(
            master,
            placeholder_text=placeholder, # texto que aparece na barra dizendo oque fazer :ex: 'digite algo aqui'
            width=largura,
            height=espessura,
            show='*' if senha else None,
            fg_color=self.cores["branco"],
            border_color=self.cores["marrom"],
            text_color=self.cores["preto"],
            corner_radius=8 # diz o quanto a borda devser arredondada

        )


    # cria um botão
    def criar_botao(self, master, texto, comando, largura=140, espessura=35, fg_cor=False, hover_cor=False, tamanho_letra=14):

        # retorna um Button (botão)
        return ctk.CTkButton(
            master,
            text=texto,
            command=comando,
            font=("Robot", tamanho_letra, "bold"),
            text_color=self.cores["branco"],
            width=largura,
            height=espessura,
            fg_color= fg_cor if fg_cor else self.cores["marrom"],
            hover_color= hover_cor if hover_cor else self.cores["marrom_escuro"],
            corner_radius=8 # diz o quanto a borda devser arredondada
            
        )


    def msgbox_incorreto(self, mensagem):
        CTkMessagebox(
            title='Aviso do Sistema', 
            message=mensagem, 
            icon='cancel', 
            option_1='Fechar',
            fg_color=self.cores["amarelo"],
            title_color=self.cores["branco"],
            text_color=self.cores["marrom_escuro"],
            button_color=self.cores["vermelho"],
            button_hover_color=self.cores["marrom"],
            border_color=self.cores["marrom_escuro"],
            border_width=4,
            header=True

        )


    def msgbox_correto(self, mensagem):
        CTkMessagebox(
            title='Aviso do Sistema',
            message=mensagem,
            icon='check',
            option_1='Fechar',
            fg_color=self.cores["azul"],
            title_color=self.cores["branco"],
            text_color=self.cores["marrom_escuro"],
            button_color=self.cores["vermelho"],
            button_hover_color=self.cores["marrom"],
            border_color=self.cores["marrom_escuro"],
            border_width=4,
            header=True
        )




if __name__ == "__main__":
    
    app = BaseWindows()
    app.msgbox_correto('Login realizado com Sucesso!')
    app.mainloop()    