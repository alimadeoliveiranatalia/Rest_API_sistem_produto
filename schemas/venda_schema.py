from pydantic import BaseModel
from datetime import datetime

class VendaBase(BaseModel):
    total: float
    data_venda_realizada: datetime
    id_vendedor: int
    id_cliente: int

class VendaCreate(VendaBase):
    pass
    
class Venda(VendaBase):
    id: int
    def __init__(self, id, total, data_venda, id_vendedor, id_cliente ):
       self.id = id
       self.total = total
       self.data_venda = data_venda
       self.id_vendedor = id_vendedor
       self.id_cliente = id_cliente 