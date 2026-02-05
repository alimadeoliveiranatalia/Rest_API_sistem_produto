from schemas.cliente_schema import Cliente

clientes = []

class ClienteRepository:

    def cadastrar_cliente(pessoa_id, data_cadastro):
        cliente = Cliente(pessoa_id, data_cadastro)
        clientes.append(cliente)
        return cliente
        
        