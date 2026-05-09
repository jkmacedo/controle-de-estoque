from src.database.connection import cria_conexao


class RepositoryUser:
    
    def __init__(self):
        pass


    def cursor(self, sql:str, valor:tuple, retorno=False):
        # tenta executar
        try:
            # abre e fecha a conexao
            with cria_conexao() as conexao:
                # abre e fecha o cursor
                with conexao.cursor() as cursor:
                    cursor.execute(sql, valor) # executa o comando sql

                    if retorno:
                        return cursor.fetchone()
                    else:
                        conexao.commit() # salva no banco de dados
                        print('Sucesso: operação realizada!')

        except Exception as erro:
            print(f'Erro na classe Repositoryuser: {erro}')


    
    def buscar_dados(self, matricula, senha): # busca dados pra verificar o so a validação do loginl
        sql = 'SELECT matricula, senha FROM usuario WHERE matricula = %s AND senha = %s AND status_user = 1'
        valores = (matricula, senha)
        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql, valores)

                    usuario = cursor.fetchone() # pegando o dado que coresponde a matricula e senha

                    if usuario:
                        return usuario # retorna a tupla com todos os valores
                    else:
                        return False
        
        except Exception as erro:
            print(f'Erro: {erro}')
            return False



    def cadastrar_usuario(self, objeto):
        sql = 'INSERT INTO usuario (matricula, senha, nome, email, telefone) VALUES (%s, %s, %s, %s, %s)'
        valores = (objeto.matricula, objeto.senha, objeto.nome, objeto.email, objeto.telefone)

        self.cursor(sql=sql, valor=valores)



    def existe_no_banco(self,coluna, valor):
        sql = f"SELECT COUNT(*) FROM usuario WHERE {coluna} = %s"
        val = (valor,)

        resultado = self.cursor(sql=sql, valor=val, retorno=True)

        return resultado[0] > 0



 

    




    



        















  
    
if __name__ == "__main__":
    
    '''
    matricula = input('matricula: ')
    senha = input('senha')
    nome = input('nome: ')
    email = input('email: ')
    telefone = input('telefone: ')



    u = Usuario(matricula=matricula, senha=senha, nome=nome, email=email, telelefone=telefone)

    r = RepositoryUser()
    r.cadastrar_usuario(u)
    '''
    r = RepositoryUser()
    usuario = r.busacar_dados(123456789, '123456789')

    print(usuario)
