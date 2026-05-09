class Usuario:
    
    def __init__(self, matricula:int, senha:str, nome:str, email:str, telelefone:str, id=None, status_user=1):
        self.id = id
        self.matricula = matricula
        self.senha = senha
        self.nome = nome
        self.email = email
        self.telefone = telelefone
        self.status = status_user

 
