from ..schemas.item_venda_schema import ItemVenda, ItemVendaCreate

items_vendas = []

items_vendas_busca = []

class ItemVendaRepository:

    def cadastrar_item_venda(self, item_data: ItemVendaCreate):
        item_venda = ItemVenda(
            id = len(items_vendas) + 1 ,
            **item_data.model_dump()
        )
        items_vendas.append(item_venda)

        return item_venda
    def buscar_itens_venda(id_produto: int , id_venda: int):
        if(id_produto):
            for item in items_vendas:
                if(item.id_produto == id_produto):
                    items_vendas_busca.append(item)
            return items_vendas_busca
        elif (id_venda):
            for item in items_vendas:
                if(item.id_venda == id_venda):
                    items_vendas_busca.append(item)
            return items_vendas_busca
        else:
            return 'Parâmetro Inválido'
item_venda_repository = ItemVendaRepository()