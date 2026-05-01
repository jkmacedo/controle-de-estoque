class Categoria:
    
    def __init__(self, categoria:str, id=None):
        self.id = id
        self.categoria = categoria
        
        

class Material:
    
    def __init__(self, nome:str, quantidade:int, enderecamento:str, id=None, id_categoria=None, cadastrado_por=None, data_cadastro=None):
        self.id = id
        self.id_categoria = id_categoria
        self.cadastrado_por = cadastrado_por
        self.data_cadastro = data_cadastro
        self.nome = nome
        self.quantidade = quantidade
        self.enderecamento = enderecamento
        
        

class SaidaMaterial:
    
    def __init__(self, quantidade_saida:int, id=None, id_usuario=None, id_material=None, data_retirada=None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_material = id_material
        self.data_retirada = data_retirada
        self.quantidade_saida = quantidade_saida