from fastapi import HTTPException
from datetime import datetime
from ..schemas.cliente_schema import ClienteCreate, Cliente
from ..repositories.pessoa_repository import PessoaRepository
from ..repositories.cliente_repository import cliente_repository

class ClienteService:

    def __init__(self):
        # Injeção de Dependências
        self.cliente = cliente_repository
        self.pessoa = PessoaRepository()
    
    def efetuar_cadastro_cliente(self, cliente_data: ClienteCreate) -> Cliente:
        """método para efetuar cadastro do cliente"""

        pessoa = self.pessoa.cadastrar_pessoa(cliente_data)

        if not pessoa:
            raise HTTPException(
                status_code=404,
                detail="Pessoa não encontrada"
            )
        cliente_info = {
            "id_pessoa": pessoa.id,
            "nome": pessoa.nome,
            "contato": pessoa.contato,
            "data_cadastro": datetime.now().date()
        }

        cliente = cliente_repository.cadastrar_cliente(cliente_info)

        return cliente
    
    def buscar_cliente(self, id_cliente: int) -> Cliente:
        """método efetua a busca de um cliente passando seu ID"""
        cliente = cliente_repository.buscar_cliente(id_cliente)

        if not cliente:
            raise HTTPException(
                status_code=404,
                detail="Cliente não Encontrado."
            )
        
        return cliente

cliente_service = ClienteService()