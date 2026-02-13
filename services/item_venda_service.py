from ..repositories.item_venda_repository import item_venda_repository
from ..schemas.item_venda_schema import ItemVendaCreate, ItemVenda

class ItemVendaService:

    def __init__(self):
        self.item = item_venda_repository

    def cadastrar_item_venda(self, item_data: ItemVendaCreate):
        item_venda = self.item.cadastrar_item_venda(item_data)
        return item_venda
    
    def buscar_item_venda(self, id_produto, id_venda):
        item_venda = self.item.buscar_itens_venda(id_produto)
        return item_venda

item_venda_service = ItemVendaCreate()