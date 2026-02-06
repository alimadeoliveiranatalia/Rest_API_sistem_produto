from fastapi import HTTPException, APIRouter, status
from schemas.venda_schema import Venda
from services.venda_service import VendaService

router = APIRouter(
    prefix="/venda",
    tags=["Vendas"]
)

@router.post(
    reponse_model=Venda,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_produto(total, data_venda, id_vendendor, id_cliente):
    venda = VendaService()
    return venda.cadastrar_venda(total,data_venda,id_vendendor,id_cliente)