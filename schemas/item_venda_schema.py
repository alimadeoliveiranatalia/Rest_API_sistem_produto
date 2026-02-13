from pydantic import BaseModel
from typing import Optional

class ItemVendaBase(BaseModel):
    id_produto: Optional[int] = None
    quantidade: Optional[int] = None
    id_venda: Optional[int] = None

class ItemVendaCreate(ItemVendaBase):
    pass

class ItemVenda(ItemVendaBase):
    id: int

    model_config = {
        "from_attributes": True
    }