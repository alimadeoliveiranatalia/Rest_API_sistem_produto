from typing import List, Optional
from schemas.vendendor_schema import Vendedor, VendendorCreate

vendendores = []

class VendendorRepository:
    
    def cadastrar_vendedor(self, vendedor_data: VendendorCreate):
        vendedor = Vendedor(
            **vendedor_data.dict()
        )
        vendendores.append(vendedor)
        return vendedor
    
    def buscar_vendedor(self, id_vendedor) -> Vendedor :
        return vendedor_repository.buscar_vendedor(id_vendedor)
    
vendedor_repository = VendendorRepository()