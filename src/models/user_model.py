class Usuario:
    
    def __init__(self, matricula:int, senha:str, nome:str, email:str, telefone:str, id=None, status_user=1):
        self.id = id
        self.matricula = matricula
        self.senha = senha
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.status = status_user

 
