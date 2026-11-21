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
                        return True

        except Exception as erro:
            print(f'Erro na classe Repositoryuser: {erro}')
            return None if retorno else False # False avisa quem chamou que não salvou


    
    def buscar_dados(self, matricula): # busca o usuário pela matrícula pra verificar a validação do login
        # não filtra mais pela senha: o banco guarda só o hash, então quem confere a senha é o controller (com bcrypt)
        # a posição [1] agora é o hash da senha, e o id continua por último
        sql = 'SELECT matricula, senha, id FROM usuario WHERE matricula = %s AND status_user = 1'
        valores = (matricula,)
        try:
            with cria_conexao() as conexao:
                with conexao.cursor() as cursor:
                    cursor.execute(sql, valores)

                    usuario = cursor.fetchone() # pegando o usuário que corresponde à matrícula

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

        return self.cursor(sql=sql, valor=valores) # True se salvou, False se deu erro



    def existe_no_banco(self,coluna, valor):
        sql = f"SELECT COUNT(*) FROM usuario WHERE {coluna} = %s"
        val = (valor,)

        resultado = self.cursor(sql=sql, valor=val, retorno=True)

        # se a consulta falhar o cursor devolve None, e aí não existe resultado[0]
        return bool(resultado) and resultado[0] > 0



 

    




    



        















  
    
if __name__ == "__main__":
    
    '''
    matricula = input('matricula: ')
    senha = input('senha')
    nome = input('nome: ')
    email = input('email: ')
    telefone = input('telefone: ')



    u = Usuario(matricula=matricula, senha=senha, nome=nome, email=email, telefone=telefone)

    r = RepositoryUser()
    r.cadastrar_usuario(u)
    '''
    r = RepositoryUser()
    usuario = r.buscar_dados(123456789)

    print(usuario)
