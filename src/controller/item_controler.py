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
        # busca os dados no database (lista vazia se não houver itens)
        for item in self.repo.buscar_itens():
            id, nome, endereco, quantidade, categoria = item
            tv.insert("", "end", values=(id, nome, endereco, quantidade, categoria))


    def total_de_itens(self):
        total = self.repo.total_de_itens()
        return total


    def retirada_material(self):
        total = self.repo.item_retirada()
        return total


    def itens_baixa_quantidade(self):
        total = self.repo.executar_consulta()
        return total


    def filtrar_treeview(self, event, tv, search):
        search = search.lower()  # Converte a pesquisa para minúsculas
        for item in tv.get_children():
            tv.delete(item)  # Limpa o Treeview antes de inserir os itens filtrados
        for item in self.repo.buscar_itens():
            id, nome, endereco, quantidade, categoria = item
            if search in nome.lower() or search in categoria.lower():
                tv.insert("", "end", values=(id, nome, endereco, quantidade, categoria))


    def adionar_ou_subtrair_estoque(self, id_material, quantidade, acao, id_usuario=None):
        if acao not in ("adicionar", "subtrair"):
            raise ValueError("Ação inválida. Use 'adicionar' ou 'subtrair'.")

        # nenhum item selecionado na tabela
        if id_material is None:
            self.bw.msgbox_incorreto(mensagem='Selecione um item na tabela primeiro!') # pop-up
            return False

        # a quantidade vem do Entry como texto, então precisa ser um número inteiro
        try:
            quantidade = int(str(quantidade).strip())
        except ValueError:
            self.bw.msgbox_incorreto(mensagem='Digite uma quantidade válida (apenas números inteiros)!') # pop-up
            return False

        if quantidade <= 0:
            self.bw.msgbox_incorreto(mensagem='A quantidade deve ser maior que zero!') # pop-up
            return False

        sucesso = self.repo.adionar_ou_subtrair_estoque(id_material, quantidade, acao, id_usuario)

        if not sucesso:
            if acao == "subtrair":
                self.bw.msgbox_incorreto(mensagem='Não foi possível dar baixa. Verifique se há estoque suficiente!') # pop-up
            else:
                self.bw.msgbox_incorreto(mensagem='Não foi possível atualizar o estoque!') # pop-up

        return sucesso
