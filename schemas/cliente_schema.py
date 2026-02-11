from datetime import datetime
from ..schemas.pessoa_schema import PessoaBase

class ClienteCreate(PessoaBase):
    pass

class Cliente(PessoaBase):
    id: int
    id_pessoa: int
    data_cadastro: datetime
    
    class Config:
       from_attributes: True
