

from src.models.user_model import Usuario
from src.repository.user_repository import RepositoryUser

def executar_teste():
    print("--- Instando Cadastro de Usuário ---")
    
    # 1. Coleta de dados
    matricula = input('Matricula: ')
    senha = input('Senha: ')
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')

    # 2. Criando o objeto Usuario (Verifique se o seu model usa 'tel=')
    u = Usuario(matricula=matricula, senha=senha, nome=nome, email=email, telelefone=telefone)

    # 3. Chamando o repositório
    r = RepositoryUser()
    r.cadastrar_usuario(u)

if __name__ == "__main__":
    executar_teste()