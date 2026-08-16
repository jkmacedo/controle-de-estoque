import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from src.controller.item_controler import ControllerItem
from src.view.base_windows import BaseWindows


class DashboardEstoque(BaseWindows):

    def __init__(self, titulo='Dashbard', largura=950, altura=550):
        super().__init__(titulo, largura, altura)

        self.control = ControllerItem()


        self.frame_principal = self.criar_frame(self,largura=950, altura=550, fg_cor=self.cores["creme"])
        self.frame_principal.place(relx=0.5, rely=0.5, anchor='center')


        self.dashboard()



    def dashboard(self):
        self.banner()
        self.banner_informativo()
        self.edit_estoque()
        self.treeview()


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
        text_total_item = self.criar_label(info_itens_cadastrados, texto="Total de Itens Cadastrados", negrito=True)
        text_total_item.place(x=110, y=20, anchor="center")

        # 1.2 cria a quantidade ---
        total_item_cad = self.criar_label(info_itens_cadastrados, tamanho_letra=40, texto=str(self.control.total_de_itens()), negrito=True)
        total_item_cad.place(x=42, y=60, anchor="center")

        # 2.1 cria texto do informativo de retiradas
        text_total_item = self.criar_label(info_itens_retirados, texto="Retiradas de Hoje", negrito=True, cor_texto=self.cores["preto"])
        text_total_item.place(x=79, y=20, anchor="center")
        
        # 2.2 cria a quantidade ---
        total_item_ret = self.criar_label(info_itens_retirados, tamanho_letra=40, texto=str(self.control.retirada_material()), negrito=True, cor_texto=self.cores["preto"])
        total_item_ret.place(x=42, y=60, anchor="center")


        # 3.1 cria texto do informativo alerta que poucos itens
        text_total_item = self.criar_label(info_itens_baixo, texto="Alerta de Estoque Baixo", negrito=True, cor_texto=self.cores["sangue"])
        text_total_item.place(x=103, y=20, anchor="center")
                
        # 3.2 cria a quantidade ---
        total_item_ret = self.criar_label(info_itens_baixo, tamanho_letra=40, texto=str(self.control.itens_baixa_quantidade()), negrito=True, cor_texto=self.cores["sangue"])
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


        # ações frame
        action_frame = self.criar_frame(frame_edit, fg_cor=self.cores["branco"], largura=250, altura=200)
        action_frame.place(relx=0.5, rely=0.5, y=0, anchor="center")
        # ações Entry
        self.qtd_item = self.criar_entry(action_frame, placeholder="Quantidade a retirar/adcionar", largura=230)
        self.qtd_item.place(relx=0.5, y=30, anchor="center")
        # botão dar baixa / retirar
        bttn_retirar = self.criar_botao(action_frame, texto="Dar baixa / Retirar", comando=None, cor_texto=self.cores["preto"], largura=230, fg_cor=self.cores["dourado"], hover_cor=self.cores["amarelo"])
        bttn_retirar.place(relx=0.5, y=80, anchor="center")
        # botão de adcionar ao estoque
        bttn_adcionar = self.criar_botao(action_frame, texto="+ Adiconar ao Estoque", comando=None, largura=230, fg_cor=self.cores["marrom_escuro"], hover_cor=self.cores["marrom"])
        bttn_adcionar.place(relx=0.5, y=120, anchor="center")


        # buttons frame
        banner_button = self.criar_frame(frame_edit, fg_cor=self.cores["cinza"], largura=250, altura=50)
        banner_button.place(relx=0.5, rely=0.5, y=125, anchor="center")
        # cria o boão de edição 
        button_edit = self.criar_botao(banner_button, comando=None, texto="[ Editar ]", largura=115, cor_texto=self.cores["preto"], fg_cor=self.cores["cinza2"], hover_cor=self.cores["branco"])
        button_edit.place(x=63, rely=0.5, anchor="center")
        # cria botão de excluir
        button_edit = self.criar_botao(banner_button, comando=None, texto="[ Excluir ]", largura=115, cor_texto=self.cores["preto"], fg_cor=self.cores["cinza2"], hover_cor=self.cores["branco"])
        button_edit.place(x=187, rely=0.5, anchor="center")

    def treeview(self):

        # freme principal do TreeView
        frame_treeview = self.criar_frame(self.frame_principal, fg_cor=self.cores["amarelo2"], largura=670, altura=310)
        frame_treeview.place(relx=0.5, rely=0.5,x=-135, y=111, anchor="center")


        search = self.criar_entry(frame_treeview, placeholder="Pesquisar por nome ou categoria", largura=630, espessura=35)
        search.place(relx=0.5, x=-18, y=21, anchor="center")
        search.bind("<KeyRelease>", lambda event: self.control.filtrar_treeview(event, self.tree, search.get()))


        # CONFIGURAÇÃO DE ESTILO DO TREEVIEW
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background=self.cores["branco"],
            foreground=self.cores["marrom_escuro"],
            rowheight=30,
            fieldbackground=self.cores["branco"]
        )

        style.configure(
            "Treeview.Heading",
            background=self.cores["marrom_escuro"],
            foreground=self.cores["amarelo"],
            font=("arial", 11, "bold"),
        )

        # treeview
        self.tree = ttk.Treeview(frame_treeview, columns=('id', 'nome', 'end', 'qtd', 'cat'), show='headings')
        self.tree.place(x=3, y=50, relwidth=0.96, relheight=0.85)

        # barra de rolagem
        barra_de_rolagem = ctk.CTkScrollbar(
            frame_treeview,
            orientation='vertical',
            command=self.tree.yview,
            fg_color='transparent',
            button_color=self.cores["branco"],
            button_hover_color=self.cores["azul"]
        )
        barra_de_rolagem.place(relx=0.96, rely=0.0, relwidth=0.04, relheight=1.0)

        # inserindo a barra de rolagem no treeview
        self.tree.configure(yscrollcommand=barra_de_rolagem.set)
        

        # configuração das colunas TITULOS
        self.tree.heading('id', text="ID")
        self.tree.heading('nome', text="NOME")
        self.tree.heading('end', text="ENDEREÇO")
        self.tree.heading('qtd', text="QUANTIDADE")
        self.tree.heading('cat', text="CATEGORIA")

        # configuração das colunas
        self.tree.column('id', width=60, anchor="center")
        self.tree.column('nome', width=220, anchor="w")
        self.tree.column('end', width=140, anchor="center")
        self.tree.column('qtd', width=90, anchor="center")
        self.tree.column('cat', width=110, anchor="center")

        self.control.Preencher_treview(tv=self.tree)

        




    




        




if __name__ == "__main__":
    ds = DashboardEstoque()
    ds.mainloop()