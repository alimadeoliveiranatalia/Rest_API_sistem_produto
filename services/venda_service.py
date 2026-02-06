from repositories.venda_repository import VendaRepository

class VendaService:
    def cadastrar_venda(total, data_venda, id_vendedor, id_cliente):
        venda = VendaRepository()
        return venda.cadastrar_venda(total, data_venda, id_vendedor, id_cliente)