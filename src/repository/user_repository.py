from src.database.connection import cria_conexao
from src.models.user_model import Usuario


class RepositoryUser:
    
    def __init__(self):
        self.conexao = cria_conexao()
        
    def cadastrar_usuario(self, objeto):
        cursor = self.conexao.cursor()
        try:
            sql = 'INSERT INTO usuario (matricula, senha, nome, email, telefone) VALUES (%s, %s, %s, %s, %s)'
            valores = (objeto.matricula, objeto.senha, objeto.nome, objeto.email, objeto.telefone)
            
            cursor.execute(sql, valores)
            
            self.conexao.commit()
            
        except Exception as erro:
            print(f'Não foi possível realisar a operação: {erro}')
            
        finally:
            cursor.close()
        
        
    
if __name__ == "__main__":
    

    matricula = input('matricula: ')
    senha = input('senha')
    nome = input('nome: ')
    email = input('email: ')
    telefone = input('telefone: ')



    u = Usuario(matricula=matricula, senha=senha, nome=nome, email=email, telelefone=telefone)

    r = RepositoryUser()
    r.cadastrar_usuario(u)