from schemas.pessoa_schema import PessoaCreate, Pessoa

pessoas = []

class PessoaRepository:
    """ Insere o registro da Pessoa no banco de dados """
    def cadastrar_pessoa(self, pessoa_data: PessoaCreate):
        novo_id = len(pessoas) + 1
        pessoa = Pessoa(
            id=novo_id,
            **pessoa_data.model_dump()
        )
        pessoas.append(pessoa)
        return pessoa
    
    def buscar_pessoa(self, id_pessoa):
        for pessoa in pessoas:
            if (pessoa.id == id_pessoa):
                return pessoa

pessoa_repository = PessoaRepository()