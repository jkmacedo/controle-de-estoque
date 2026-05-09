import mysql.connector
import os
from dotenv import load_dotenv

# carrega as senhas do meu banco de dados do meu arquivo .env
load_dotenv()

def cria_conexao():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            port=os.getenv("DB_PORT"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NOME"),
        )

        if conexao.is_connected():
            print('Sucesso: conectado ao banco de dados!')
            return conexao
        
    except Exception as erro:
        print(f'Falha: Erro ao conectar: {erro}')




if __name__ == "__main__":
    cria_conexao()