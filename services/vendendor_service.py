from ..schemas.vendendor_schema import VendendorCreate, Vendedor
from ..repositories.vendendor_repository import vendedor_repository

class VendendorService:
    
    def cadastrar_vendendor(self, vendedor_data: VendendorCreate) -> Vendedor:
        vendendor = vendedor_repository.cadastrar_vendedor(vendedor_data)
        return vendendor
    
    def buscar_vendedor(self, id_vendedor: int) -> Vendedor :
        return vendedor_repository.buscar_vendedor(id_vendedor)
    
vendedor_service = VendendorService()