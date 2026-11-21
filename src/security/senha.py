import bcrypt

# o bcrypt só olha os primeiros 72 bytes da senha, então o cadastro não aceita mais que isso
TAMANHO_MAXIMO_BYTES = 72


def gerar_hash(senha: str) -> str:
    # transforma a senha em um hash (texto de ~60 caracteres) que é o que vai pro banco
    # o gensalt() cria um "sal" aleatório a cada chamada e ele já fica dentro do próprio hash,
    # por isso duas pessoas com a mesma senha acabam com hashes diferentes
    hash_bytes = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())
    return hash_bytes.decode("utf-8")


def senha_confere(senha_digitada: str, hash_salvo: str) -> bool:
    # confere a senha digitada com o hash que está no banco
    # o bcrypt pega o sal de dentro do hash salvo, gera um hash da senha digitada e compara os dois
    try:
        return bcrypt.checkpw(senha_digitada.encode("utf-8"), hash_salvo.encode("utf-8"))
    except ValueError:
        # acontece se o valor salvo no banco não for um hash (ex.: senha antiga ainda em texto puro)
        # ou se a senha digitada passar de 72 bytes; nos dois casos o login deve ser recusado
        return False


def ja_e_hash(texto: str) -> bool:
    # todo hash do bcrypt tem 60 caracteres e começa com $2a$, $2b$ ou $2y$
    # o script de migração usa isso pra não converter duas vezes a mesma senha
    return len(texto) == 60 and texto.startswith(("$2a$", "$2b$", "$2y$"))
