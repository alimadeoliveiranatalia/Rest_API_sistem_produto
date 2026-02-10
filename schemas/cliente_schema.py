from pydantic import BaseModel
from datetime import date
from schemas.pessoa_schema import Pessoa

class ClienteBase(BaseModel):
    id_pessoa: int
    data_cadastro: date

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    
    class Config:
       orm_mode: True


#class Cliente():
#    def __init__(self, id_pessoa, datacadastro):
#        self.id_pessoa= id_pessoa,
#        self.data_cadastro=datacadastro
