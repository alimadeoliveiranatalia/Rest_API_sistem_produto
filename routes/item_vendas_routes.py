from fastapi import HTTPException, APIRouter, status
from ..schemas.item_venda_schema import ItemVenda, ItemVendaCreate
from ..services.item_venda_service import item_venda_service

router = APIRouter(
    prefix="/item_venda",
    tags=["Itens Vendas"]
)

@router.post(
    "/",
    response_model=ItemVenda,
    status_code=status.HTTP_201_CREATED
)
def registrar_item_venda(item_data: ItemVendaCreate):
    item_venda = item_venda_service.cadastrar_item_venda(item_data)
    return item_venda
@router.get(
    "/{id_venda}/{id_produto}",
    response_model=ItemVenda,
    status_code=200,
)
def buscar_item_venda(id_produto, id_venda):
    item = item_venda_service.buscar_item_venda(id_produto=id_produto)
    return item