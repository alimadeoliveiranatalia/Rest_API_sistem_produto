from pydantic import BaseModel

class PessoaBase(BaseModel):
    nome: str
    contato: str

class PessoaCreate(PessoaBase):
    pass

class Pessoa(PessoaBase):
    id: int

    class Confi:
        from_attributes: True