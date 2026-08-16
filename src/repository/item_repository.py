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
            return 0



    def total_de_itens(self):
        sql = "SELECT COUNT(*) FROM material;"
        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql)
                    total = cursor.fetchone()[0]  # pega o primeiro elemento da tupla retornada
                    return total
        except Exception as erro:
            print(f"Erro: {erro}")
            return 0


    def item_retirada(self):
        sql = "SELECT COUNT(*) AS retiradas_hoje FROM saida_material WHERE DATE(data_retirada) = CURDATE();"
        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql)
                    total = cursor.fetchone()[0]  # pega o primeiro elemento da tupla retornada
                    return total
        except Exception as erro:
            print(f"Erro: {erro}")
            return 0


    def executar_consulta(self):
        sql = "SELECT COUNT(*) AS baixa_quantidade FROM material WHERE quantidade < 10;"
        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql)
                    total = cursor.fetchone()[0]  # pega o primeiro elemento da tupla retornada
                    return total
        except Exception as erro:
            print(f"Erro: {erro}")
            return 0

    def adionar_ou_subtrair_estoque(self, id_material, quantidade, acao):
        if acao == "adicionar":
            sql = "UPDATE material SET quantidade = quantidade + %s WHERE id = %s"
        elif acao == "subtrair":
            sql = "UPDATE material SET quantidade = quantidade - %s WHERE id = %s"
        else:
            raise ValueError("Ação inválida. Use 'adicionar' ou 'subtrair'.")

        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql, (quantidade, id_material))
                    conexao.commit()
                    return True
        except Exception as erro:
            print(f"Erro: {erro}")
            return False
