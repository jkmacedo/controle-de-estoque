"""
Converte as senhas que já estão salvas em texto puro no banco para hash (bcrypt).

Rode UMA vez, a partir da pasta raiz do projeto, depois de instalar o bcrypt:
    python -m scripts.migrar_senhas

Pode rodar de novo sem medo: o que já é hash é pulado, então nada é convertido duas vezes.
Se preferir, apague os usuários de teste e cadastre de novo em vez de usar este script.
Faça um backup do banco antes, porque o hash não volta a ser a senha original.
"""
from src.database.connection import cria_conexao
from src.security.senha import gerar_hash, ja_e_hash, TAMANHO_MAXIMO_BYTES


def migrar():
    convertidos = 0
    ja_eram_hash = 0
    pulados = []  # usuários cuja senha antiga não pode virar hash (maior que o limite do bcrypt)

    with cria_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, senha FROM usuario")
            usuarios = cursor.fetchall()

            for id_usuario, senha in usuarios:
                if ja_e_hash(senha):
                    ja_eram_hash += 1
                    continue

                if len(senha.encode("utf-8")) > TAMANHO_MAXIMO_BYTES:
                    pulados.append(id_usuario)
                    continue

                cursor.execute("UPDATE usuario SET senha = %s WHERE id = %s", (gerar_hash(senha), id_usuario))
                convertidos += 1

        # só salva no fim: se der erro no meio, nenhuma senha fica pela metade
        conexao.commit()

    print(f"Convertidas: {convertidos} | Já eram hash: {ja_eram_hash} | Puladas (maiores que 72 bytes): {pulados}")


if __name__ == "__main__":
    migrar()
