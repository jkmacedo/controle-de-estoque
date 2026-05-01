from src.database.connection import cria_conexao
from src.models.user_model import Usuario


class RepositoryUser:
    
    def __init__(self):
        pass


    def cursor(self, sql:str, valor:tuple):
        # tenta executar
        try:
            # abre e fecha a conexao
            with cria_conexao() as conexao:
                # abre e fecha o cursor
                with conexao.cursor() as cursor:
                    cursor.execute(sql, valor) # executa o comando sql
                    conexao.commit() # salva no banco de dados
                    print('Sucesso: operação realizada!')

        except Exception as erro:
            print(f'Erro na classe Repositoryuser: {erro}')

    

    def buscar_dados(self, objeto):
        sql = 'SELECT * FROM usuario WHERE matricula = %s AND senha = %s'
        valores = (objeto.matricula, objeto.senha)

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


    def cadastrar_usuario(self, objeto):
        sql = 'INSERT INTO usuario (matricula, senha, nome, email, telefone) VALUES (%s, %s, %s, %s, %s)'
        valores = (objeto.matricula, objeto.senha, objeto.nome, objeto.email, objeto.telefone)

        self.cursor(sql=sql, valor=valores)


    def atualizar_dados_usuario(self, oque_mudar:str, id:str, novo_dado:str):

        if oque_mudar.lower() =='nome': # mudar nome
            sql = 'UPDATE usuario SET nome = %s WHERE id = %s'

        elif oque_mudar.lower() =='email': # mudar email
            sql = 'UPDATE usuario SET email = %s WHERE id = %s'

        elif oque_mudar.lower() =='telefone': # mudar telefone
            sql = 'UPDATE usuario SET telefone = %s WHERE id = %s'

        elif oque_mudar.lower() =='senha': # mudar senha
            sql = 'UPDATE usuario SET senha = %s WHERE id = %s'


        valores = (novo_dado, id) # o novo valor e o id do item que vaiser alterado
        self.cursor(sql=sql, valor=valores)




    



        















  
    
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
