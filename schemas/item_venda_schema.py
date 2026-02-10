from pydantic import BaseModel


class ItemVendaBase(BaseModel):
    id_produto: int
    quantidade: int
    id_venda: int

class ItemVendaCreate(ItemVendaBase):
    pass

class ItemVenda(ItemVendaBase):
    id: int

    class Config:
       from_attributes: True