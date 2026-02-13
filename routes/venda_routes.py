from fastapi import HTTPException, APIRouter, status
from ..schemas.venda_schema import Venda, VendaCreate
from ..services.venda_service import venda_service

router = APIRouter(
    prefix="/venda",
    tags=["Vendas"]
)

@router.post(
    "/",
    response_model=Venda,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_produto(venda_data: VendaCreate):
    venda = venda_service.cadastrar_venda(venda_data)
    return venda

@router.get(
    "/{id_vendedor}/{id_cliente}/{data_realizada}",
    response_model=Venda,
    status_code=200
)
def buscar_vendas(id_vendedor: int, id_cliente: int, data_realizada: str):
    venda = venda_service.buscar_produto(id_vendedor=id_vendedor)
    return venda