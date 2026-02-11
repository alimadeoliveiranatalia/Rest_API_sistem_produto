from ..schemas.vendedor_schema import Vendedor, VendedorCreate

vendedores = []

class VendedorRepository:
    def cadastrar_vendedor(self, vendedor_data: VendedorCreate):
        """Efetua a inserção de um registro de Vendedor no Banco de Dados."""
        novo_id = len(vendedores) + 1
        vendedor = Vendedor(
            id = novo_id,
            **vendedor_data
        )
        vendedores.append(vendedor)
        return vendedor
    
    def buscar_vendedor(self, id_vendedor) -> Vendedor :
        """Efetua a busca de um vendedor no Banco de Dados."""
        for vendedor in vendedores:
            if (vendedor.id == id_vendedor):
                return vendedor
    
vendedor_repository = VendedorRepository()