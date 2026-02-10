from typing import List, Optional
from schemas.cliente_schema import ClienteCreate, Cliente
from repositories.cliente_repository import cliente_repository

class ClienteService:
    
    def efetuar_cadastro_cliente(self, cliente_data: ClienteCreate) -> Cliente:
        """método para efetuar cadastro do cliente"""
        return cliente_repository.cadastrar_cliente(cliente_data)
    
    def buscar_cliente(self, id_cliente: int) -> Cliente:
        """método efetua a busca de um cliente passando seu ID"""
        return cliente_repository.buscar_cliente(id_cliente)

cliente_service = ClienteService()