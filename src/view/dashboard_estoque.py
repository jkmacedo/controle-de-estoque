import customtkinter as ctk
from src.view.base_windows import BaseWindows

class DashboardEstoque(BaseWindows):

    def __init__(self, titulo='Dashdbard', largura=950, altura=550):
        super().__init__(titulo, largura, altura)

        self.frame_principal = self.criar_frame(self,largura=950, altura=550, fg_cor=self.cores["creme"])
        self.frame_principal.place(relx=0.5, rely=0.5, anchor='center')


        self.dashboard()



    def dashboard(self):
        self.banner()
        self.banner_informativo()


    def banner(self):

        #  Cria o frame pai (marrom)
        banner_outblack_main = self.criar_frame(self.frame_principal, fg_cor=self.cores["marrom_escuro"], largura=940, altura=110)
        banner_outblack_main.place(relx=0.5, rely=0.5, y=-220, anchor="center")
        
        # Cria o frame filho (branco)
        banner_frontwhite_secund = self.criar_frame(banner_outblack_main, fg_cor=self.cores["branco"], largura=1300, altura=80)
        banner_frontwhite_secund.place(relx=0, rely=0.5, y=13.5,anchor="center")

        # Cria o texto no frame filho (branco)
        marrom = self.cores["marrom_escuro"]
        text_ga = self.criar_label(banner_frontwhite_secund, texto="Gestão de Almoxarifado", tamanho_letra=30, negrito=True, cor_texto=marrom)
        text_ga.place(relx=0.5, rely=0.5,x=200, anchor="center")

        # cria botão de cadastrar novo usuario
        cor_bttn = self.cores["amarelo"]
        cor_bttn_text = self.cores["marrom"]
        cor_hover = self.cores["creme"]
        bttn_novo_item = self.criar_botao(banner_outblack_main, texto="+ Cadastrar Novo Item", cor_texto=cor_bttn_text, fg_cor=cor_bttn, hover_cor=cor_hover, comando=None)
        bttn_novo_item.place(relx=1, rely=0.5, x=-100, y=25, anchor='center')

    def banner_informativo(self):

        # criar frame que vai guardar os informativos de total de itens, retiradas e baixa quantidade.
        frame_informativo = self.criar_frame(self.frame_principal, fg_cor=self.cores["amarelo2"], largura=940, altura=110)
        frame_informativo.place(relx=0.5, rely=0.5, y=-100, anchor="center")

        # cria o informativo da quantidad de item cadastrados
        info_itens_cadastrados = self.criar_frame(frame_informativo, fg_cor=self.cores["marrom_escuro"], largura=300, altura=90)
        info_itens_cadastrados.place(relx=0.5, rely=0.5, x=-310, anchor="center")

        # cria o informativo da quantidad de item retirados
        info_itens_retirados = self.criar_frame(frame_informativo, fg_cor=self.cores["dourado"], largura=300, altura=90)
        info_itens_retirados.place(relx=0.5, rely=0.5, x=0, anchor="center")

        # cria o informativo da quantidad de item com baixa quantidade
        info_itens_baixo = self.criar_frame(frame_informativo, fg_cor=self.cores["vermelho2"], largura=300, altura=90)
        info_itens_baixo.place(relx=0.5, rely=0.5, x=310, anchor="center")








if __name__ == "__main__":
    ds = DashboardEstoque()
    ds.mainloop()