from fastapi import HTTPException
from schemas.vendedor_schema import VendedorCreate, Vendedor
from repositories.pessoa_repository import PessoaRepository
from repositories.vendedor_repository import vendedor_repository
from datetime import datetime

class VendedorService:

    def __init__(self) :
        self.pessoa = PessoaRepository()
        self.vendedor = vendedor_repository
    
    def cadastrar_vendedor(self, vendedor_data: VendedorCreate) -> Vendedor:
        
        pessoa = self.pessoa.cadastrar_pessoa(vendedor_data)

        if not pessoa:
            raise HTTPException(status_code=404, detail="Pessoa não encontrada")
        
        print(pessoa)
        vendedor_info = {
            "id_pessoa": pessoa.id,
            "nome": pessoa.nome,
            "contato": pessoa.contato,
            "data_cadastro": datetime.now().date()
        }
        print(vendedor_info)
        
        vendedor = self.vendedor.cadastrar_vendedor(vendedor_info)
        
        return vendedor
    
    def buscar_vendedor(self, id_vendedor: int) -> Vendedor :
        return vendedor_repository.buscar_vendedor(id_vendedor)
    
vendedor_service = VendedorService()