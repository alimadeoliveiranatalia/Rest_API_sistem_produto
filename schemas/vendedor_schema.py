from schemas.pessoa_schema import PessoaBase
from datetime import datetime

class VendedorCreate(PessoaBase):
    pass

class Vendedor(PessoaBase):
    id: int
    id_pessoa: int
    data_cadastro: datetime
    
    class Config:
       orm_mode: True