from src.database.connection import cria_conexao


class RepositoryItem:
    
    def __init__(self):
        pass


    def buscar_itens(self):  # busca dados pra verificar o so a validação do loginl
        sql = "SELECT m.id, m.nome_produto, m.endereçamento, m.quantidade, c.nome_categoria FROM material m INNER JOIN categoria c ON m.id_categoria = c.id;"
        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql)

                    emEstoque = cursor.fetchall()  # pegando o dado que coresponde a matricula e senha

                    if emEstoque:
                        return emEstoque  # retorna a tupla com todos os valores
                    else:
                        return False

        except Exception as erro:
            print(f"Erro: {erro}")
            return False






