from fastapi import HTTPException
from ..schemas.vendedor_schema import VendedorCreate, Vendedor
from ..repositories.pessoa_repository import PessoaRepository
from ..repositories.vendedor_repository import vendedor_repository
from datetime import datetime

class VendedorService:

    def __init__(self):
        # Injeção de Dependências
        self.vendedor = vendedor_repository
        self.pessoa = PessoaRepository()
    
    def cadastrar_vendendor(self, vendedor_data: VendedorCreate) -> Vendedor:
        """Cadastra Vendedor no Sistema"""
        
        pessoa = self.pessoa.cadastrar_pessoa(vendedor_data)
        
        if not pessoa:
           raise HTTPException(
              status_code=404,
              detail="Pessoa não encontrada"
           )        
               
        vendedor_info = {
            "id_pessoa": pessoa.id,
            "nome": pessoa.nome,
            "contato": pessoa.contato,
            "data_cadastro": datetime.now().date()
        }

        vendedor = self.vendedor.cadastrar_vendedor(vendedor_info)
        
        return vendedor
    
    def buscar_vendedor(self, id_vendedor: int) -> Vendedor :
        """Busca de um vendedor no sistema passando o seu ID"""
        vendedor = vendedor_repository.buscar_vendedor(id_vendedor)
        if not vendedor:
            raise HTTPException(
                status_code=404,
                detail="Vendedor não Encontrado."
            )
        return vendedor
    
vendedor_service = VendedorService()