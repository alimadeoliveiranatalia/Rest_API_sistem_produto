from ..schemas.venda_schema import Venda, VendaCreate

vendas = []

vendas_busca = []

class VendaRepository:

    def cadastrar_venda(self, venda_data: VendaCreate):
        """ Efetua o registro de uma venda no banco de dados."""
        
        venda = Venda(
            id = len(vendas) + 1,
            **venda_data.model_dump()
        )

        vendas.append(venda)
        return venda
    def buscar_vendas(data_realizada, id_vendedor, id_cliente):
        if(data_realizada):
            for venda in vendas:
                if(venda.data_venda_realizada == data_realizada):
                    vendas_busca.append(venda)
            return vendas_busca
        elif(id_vendedor):
           for venda in vendas:
                if(venda.id_vendedor == id_vendedor):
                    vendas_busca.append(venda)
                return vendas_busca
        elif(id_cliente):
            for venda in vendas:
                if(venda.id_cliente == id_cliente):
                    vendas_busca.append(venda)
            return vendas_busca 
        else:
            return 'Parâmetro de busca Inválido.'

venda_repository = VendaRepository()
        