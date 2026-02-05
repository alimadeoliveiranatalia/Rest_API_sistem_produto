from repositories.cliente_repository import ClienteRepository

class ClienteService:
    
    def efetuar_cadastro_cliente(pessoa_id, data_cadastro):
        """método para efetuar cadastro do cliente"""
        cliente = ClienteRepository()
        return cliente.cadastrar_cliente(pessoa_id, data_cadastro)
