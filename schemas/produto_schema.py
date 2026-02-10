from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome_identificacao: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int

    class Config:
       from_attributes: True
