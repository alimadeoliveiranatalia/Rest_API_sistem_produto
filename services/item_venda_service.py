from repositories.item_venda_repository import ItemVendaRepository

class ItemVendaService:
    def cadastrar_item_venda(id_produto, quantidade, id_venda):
        item_venda = ItemVendaRepository()
        return item_venda.cadastrar_item_venda(id_produto, quantidade, id_venda)