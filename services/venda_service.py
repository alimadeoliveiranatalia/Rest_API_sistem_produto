from ..schemas.venda_schema import Venda, VendaCreate
from ..repositories.venda_repository import venda_repository

class VendaService:

    def __init__(self):
        self.venda = venda_repository

    def cadastrar_venda(self, venda_data: VendaCreate):
        """Efetua um cadastro de Venda"""
        venda = self.venda.cadastrar_venda(venda_data)
        return venda
    
    def buscar_produto(self, id_vendedor):
        venda = self.venda.buscar_vendas(id_vendedor=id_vendedor)

        return venda
    
venda_service = VendaService()