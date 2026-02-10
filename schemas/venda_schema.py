from pydantic import BaseModel

class VendaBase(BaseModel):
    id: int
    total: float
    data_venda: str
    id_vendedor: int
    id_cliente: int
class VendaCreate(VendaBase):
    pass

class Venda(VendaBase):
    id: int

    class Config:
        from_attributes = True
