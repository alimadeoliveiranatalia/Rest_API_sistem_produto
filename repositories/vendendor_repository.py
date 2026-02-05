from schemas.vendendor_schema import Vendedor

vendendores = []

class VendendorRepository:
    
    def cadastrar_vendedor(pessoa_id, data_cadastro):
        vendedor = Vendedor(pessoa_id, data_cadastro)
        vendendores.append(vendedor)
        return vendedor