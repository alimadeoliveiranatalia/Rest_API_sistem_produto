from typing import List, Optional
from ..schemas.cliente_schema import ClienteCreate, Cliente

clientes = []

class ClienteRepository:

    def cadastrar_cliente(self, cliente_data: ClienteCreate) -> Cliente :
        """ Insere o registro do Cliente no banco de dados """
        novo_cliente = Cliente(
            **cliente_data.dict()
        )
        clientes.append(novo_cliente)
        return novo_cliente
        
cliente_repository = ClienteRepository()
        