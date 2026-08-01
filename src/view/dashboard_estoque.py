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
        self.edit_estoque()


    def banner(self):

        #  Cria o frame pai (marrom)
        banner_outblack_main = self.criar_frame(self.frame_principal, fg_cor=self.cores["marrom_escuro"], largura=940, altura=110)
        banner_outblack_main.place(relx=0.5, rely=0.5, y=-220, anchor="center")
        
        # Cria o frame filho (branco)
        banner_frontwhite_secund = self.criar_frame(banner_outblack_main, fg_cor=self.cores["branco"], largura=1300, altura=80, borda=True)
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

        # 1 cria o informativo da quantidade de item cadastrados
        info_itens_cadastrados = self.criar_frame(frame_informativo, fg_cor=self.cores["marrom_escuro"], largura=300, altura=90)
        info_itens_cadastrados.place(relx=0.5, rely=0.5, x=-310, anchor="center")

        # 2 cria o informativo da quantidad de item retirados
        info_itens_retirados = self.criar_frame(frame_informativo, fg_cor=self.cores["dourado"], largura=300, altura=90)
        info_itens_retirados.place(relx=0.5, rely=0.5, x=0, anchor="center")

        # 3 cria o informativo da quantidad de item com baixa quantidade
        info_itens_baixo = self.criar_frame(frame_informativo, fg_cor=self.cores["vermelho2"], largura=300, altura=90)
        info_itens_baixo.place(relx=0.5, rely=0.5, x=310, anchor="center")

        # QUANTIDADES

        # 1.1 cria texto do informativo de quantidade
        text_total_item = self.criar_label(info_itens_cadastrados, texto="Total de Itens Cadastrado", negrito=True)
        text_total_item.place(x=110, y=20, anchor="center")

        # 1.2 cria a quantidade ---
        total_item_cad = self.criar_label(info_itens_cadastrados, tamanho_letra=40, texto="100", negrito=True)
        total_item_cad.place(x=42, y=60, anchor="center")

        # 2.1 cria texto do informativo de retiradas
        text_total_item = self.criar_label(info_itens_retirados, texto="Retiradas de Hoje", negrito=True, cor_texto=self.cores["preto"])
        text_total_item.place(x=79, y=20, anchor="center")
        
        # 2.2 cria a quantidade ---
        total_item_ret = self.criar_label(info_itens_retirados, tamanho_letra=40, texto="100", negrito=True, cor_texto=self.cores["preto"])
        total_item_ret.place(x=42, y=60, anchor="center")


        # 3.1 cria texto do informativo alerta que poucos itens
        text_total_item = self.criar_label(info_itens_baixo, texto="Alerta de Estoque Baixo", negrito=True, cor_texto=self.cores["sangue"])
        text_total_item.place(x=103, y=20, anchor="center")
                
        # 3.2 cria a quantidade ---
        total_item_ret = self.criar_label(info_itens_baixo, tamanho_letra=40, texto="100", negrito=True, cor_texto=self.cores["sangue"])
        total_item_ret.place(x=42, y=60, anchor="center")

    def edit_estoque(self):

        # frame pricipal
        frame_edit = self.criar_frame(self.frame_principal, fg_cor=self.cores["amarelo2"], largura=268, altura=310)
        frame_edit.place(relx=1, rely=0.5,x=-140, y=112, anchor="center")
        

        # banner frame
        banner = self.criar_frame(frame_edit, fg_cor=self.cores["marrom"], largura=250, altura=60)
        banner.place(relx=0.5, rely=0.5, y=-120, anchor="center")
        # banner texto label
        text_banner = self.criar_label(banner, texto="Ações de Movimentação",tamanho_letra=18, negrito=True)
        text_banner.place(relx=0.5, rely=0.5, anchor="center")















        # buttons frame
        banner_button = self.criar_frame(frame_edit, fg_cor=self.cores["cinza"], largura=250, altura=50)
        banner_button.place(relx=0.5, rely=0.5, y=125, anchor="center")
        # cria o boão de edição 
        button_edit = self.criar_botao(banner_button, comando=None, texto="[ Editar ]", largura=115, cor_texto=self.cores["preto"], fg_cor=self.cores["cinza2"], hover_cor=self.cores["branco"])
        button_edit.place(x=63, rely=0.5, anchor="center")
        # cria botão de excluir
        button_edit = self.criar_botao(banner_button, comando=None, texto="[ Excluir ]", largura=115, cor_texto=self.cores["preto"], fg_cor=self.cores["cinza2"], hover_cor=self.cores["branco"])
        button_edit.place(x=187, rely=0.5, anchor="center")








if __name__ == "__main__":
    ds = DashboardEstoque()
    ds.mainloop()