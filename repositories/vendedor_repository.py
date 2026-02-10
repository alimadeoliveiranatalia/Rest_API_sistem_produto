from typing import List, Optional
from schemas.vendedor_schema import VendedorCreate, Vendedor

vendedores = []

class VendedorRepository:
    
    def cadastrar_vendedor(self, vendedor_data: VendedorCreate):
        vendedor = Vendedor(
            id= len(vendedores) + 1,
            **vendedor_data
        )
        vendedores.append(vendedor)
        return vendedor
    
    def buscar_vendedor(self, id_vendedor) -> Vendedor :
        for vendedor in vendedores:
            if (vendedor.id == id_vendedor):
                return vendedor
    
vendedor_repository = VendedorRepository()