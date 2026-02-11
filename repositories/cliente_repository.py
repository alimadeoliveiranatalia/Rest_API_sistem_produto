from typing import List, Optional
from ..schemas.cliente_schema import ClienteCreate, Cliente

clientes = []

class ClienteRepository:

    def cadastrar_cliente(self, cliente_data: ClienteCreate) -> Cliente :
        """ Insere o registro do Cliente no banco de dados """
        novo_cliente = Cliente(
            id = len(clientes) + 1,
            **cliente_data.model_dump()
        )
        clientes.append(novo_cliente)
        return novo_cliente
    def buscar_cliente(self, id_cliente: int) -> Cliente:
        """Busca o cliente no banco de Dados passando seu Parâmetro"""
        for cliente in clientes:
            if (cliente.id == id_cliente):
                return cliente
        
        
cliente_repository = ClienteRepository()
        