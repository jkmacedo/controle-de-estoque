

from src.models.user_model import Usuario
from src.repository.user_repository import RepositoryUser

def executar_teste():

    r = RepositoryUser()
    print("--- Instando Cadastro de Usuário ---")


    print('''
    [1] buscar
    [2] cadatrar
    [3] atualizar
             ''')
    
    escolha = input('>>>> ')
    if escolha =='1':
        u = Usuario(matricula=123456789, senha='123456789',nome='fulano', email='fulado@gamil.com', telelefone='(12) 98888-8888')
        dados = r.buscar_dados(u)
        print(dados)

    elif escolha == '2':
         
        u = Usuario(matricula=123456779, senha='123456779',nome='fulano', email='fulado@gamil.com', telelefone='(12) 98888-8888')
        r.cadastrar_usuario(u)

    elif escolha == '3':
        r.atualizar_dados_usuario(oque_mudar='email', id='1', novo_dado='kayky123@gmail.com')

    
   

    

if __name__ == "__main__":
    executar_teste()