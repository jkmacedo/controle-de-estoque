import customtkinter as ctk


class BaseWindows(ctk.CTk):
    # Definir método construtor
    def __init__(self, titulo='nome da janela', largura=400, altura=500):
        # Herda atributos da classe pai (Ctk)
        super().__init__()


        # cria a paleta de cores do projeto
        self.cores = {
            "marrom": "#63493C",
            "marrom_escuro": "#4A362D",
            "creme": "#F5E6D3",
            "amarelo": "#FFB800",
            "preto": "#000000",
            "branco": "#FFFFFF"
        }

        self.title(titulo) # titulo
        self.geometry(f'{largura}x{altura}') # define o tamanho da janela
        self.configure(fg_color=self.cores["creme"]) # define a cor de fundo daa janela
        self.resizable(False, False) # não deixar o usuario esticar nem pra cima ou pra baixo

        # definir configurações para os itens na janela se adaptarem ao tamanho da janela
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


    # Função para criar texto;
    def criar_label(self, master, texto, tamanho_letra=16, negrito=False, cor_texto="marrom"):

        # retorna um label (texto)
        return ctk.CTkLabel(
            master,
            text=texto,
            font= ("Roboto", tamanho_letra, "bold" if negrito else "normal"),
            text_color=self.cores[f"{cor_texto}"]

        )


    # cria a barra de digitar
    def criar_entry(self, master, placeholder, largura=300, senha=False):

        # retorna o Entry (barra)
        return ctk.CTkEntry(
            master,
            placeholder_text=placeholder, # texto que aparece na barra dizendo oque fazer :ex: 'digite algo aqui'
            width=largura,
            height=40,
            show='*' if senha else None,
            fg_color=self.cores["branco"],
            border_color=self.cores["marrom"],
            text_color=self.cores["preto"],
            corner_radius=8 # diz o quanto a borda devser arredondada

        )


    # cria um botão
    def criar_botao(self, master, texto, comando, largura=140, fg_cor="marrom", hover_cor="marrom_escuro", tamanho_letra=14):

        # retorna um Button (botão)
        return ctk.CTkButton(
            master,
            text=texto,
            command=comando,
            font=("Robot", tamanho_letra, "bold"),
            text_color=self.cores["branco"],
            width=largura,
            height=35,
            fg_color=self.cores[f"{fg_cor}"],
            hover_color=self.cores[f"{hover_cor}"],
            corner_radius=8 # diz o quanto a borda devser arredondada
            
        )







if __name__ == "__main__":
    app = BaseWindows()
    app.mainloop()    