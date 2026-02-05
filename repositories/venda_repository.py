from schemas.venda_schema import Venda

vendas = []

class VendaRepository:

    def cadastrar_venda(total, vendendor_id):
        venda = Venda(total, vendendor_id)
        vendas.append(venda)
        return venda