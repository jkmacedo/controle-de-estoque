from src.database.connection import cria_conexao


class RepositoryItem:

    def __init__(self):
        pass


    def buscar_itens(self):  # busca todos os materiais com o nome da categoria
        # LEFT JOIN pra não esconder materiais sem categoria (o total de itens conta todos)
        sql = "SELECT m.id, m.nome_produto, m.endereçamento, m.quantidade, COALESCE(c.nome_categoria, 'Sem categoria') FROM material m LEFT JOIN categoria c ON m.id_categoria = c.id;"
        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql)
                    return cursor.fetchall()  # lista de tuplas (lista vazia se não houver itens)

        except Exception as erro:
            print(f"Erro: {erro}")
            return []



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

    def adionar_ou_subtrair_estoque(self, id_material, quantidade, acao, id_usuario=None):
        if acao == "adicionar":
            # COALESCE porque a coluna quantidade aceita NULL (NULL + 5 continuaria NULL)
            sql = "UPDATE material SET quantidade = COALESCE(quantidade, 0) + %s WHERE id = %s"
            valores = (quantidade, id_material)
        elif acao == "subtrair":
            # só subtrai se tiver quantidade suficiente, pra o estoque nunca ficar negativo
            sql = "UPDATE material SET quantidade = quantidade - %s WHERE id = %s AND quantidade >= %s"
            valores = (quantidade, id_material, quantidade)
        else:
            raise ValueError("Ação inválida. Use 'adicionar' ou 'subtrair'.")

        # quantidade zero ou negativa não faz sentido (e negativa inverteria a operação)
        if quantidade <= 0:
            return False

        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql, valores)

                    # nenhuma linha alterada = material não existe ou estoque insuficiente
                    if cursor.rowcount == 0:
                        conexao.rollback()
                        return False

                    # toda retirada fica registrada na tabela de saídas (usada no card "Retiradas de Hoje")
                    if acao == "subtrair":
                        cursor.execute(
                            "INSERT INTO saida_material (id_usuario, id_material, quantidade_retirada) VALUES (%s, %s, %s)",
                            (id_usuario, id_material, quantidade)
                        )

                    # baixa no estoque e registro da saída são salvos juntos
                    conexao.commit()
                    return True
        except Exception as erro:
            print(f"Erro: {erro}")
            return False
