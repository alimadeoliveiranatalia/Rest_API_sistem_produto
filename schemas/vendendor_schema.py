from pydantic import BaseModel
from datetime import datetime

class VendedorBase(BaseModel):
    id_pessoa: int
    data_cadastro: datetime

class VendendorCreate(VendedorBase):
    pass

class Vendedor(VendedorBase):
    id: int