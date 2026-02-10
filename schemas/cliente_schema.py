from pydantic import BaseModel
from datetime import date
from schemas.pessoa_schema import PessoaBase

class ClienteCreate(PessoaBase):
    pass

class Cliente(PessoaBase):
    id: int
    id_pessoa: int
    data_cadastro: date
    
    class Config:
       orm_mode: True
