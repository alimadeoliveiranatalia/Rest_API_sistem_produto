from fastapi import HTTPException, APIRouter, status
from schemas.item_venda_schema import ItemVenda
from services.item_venda_service import ItemVendaService

router = APIRouter(
    prefix="/item_venda",
    tags=["Itens Vendas"]
)

@router.post(
    "/",
    response_model=ItemVenda,
    status_code=status.HTTP_201_CREATED
)
def registrar_item_venda(id_produto, quantidade, id_venda):
    item_venda = ItemVendaService()
    return item_venda.cadastrar_item_venda(id_produto, quantidade, id_venda)