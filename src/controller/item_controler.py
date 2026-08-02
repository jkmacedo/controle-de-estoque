from src.repository.item_repository import RepositoryItem
from src.view.base_windows import BaseWindows
from src.models.item_model import Categoria, Material, SaidaMaterial

class ControllerItem:

    def __init__(self):
        self.repo = RepositoryItem()
        self.bw = BaseWindows()


    def Preencher_treview(self, tv):

            # limpa o treeview antes inserir
            for i in tv.get_children():
                tv.delete(i)

            # busca os dados no database
            emEstoque = self.repo.buscar_itens()
            # inseri o item
            for item in emEstoque:
                id, nome, endereco, quantidade, categoria = item
                tv.insert("", "end", values=(id, nome, endereco, quantidade, categoria))


    