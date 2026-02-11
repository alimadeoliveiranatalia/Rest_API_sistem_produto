from fastapi import APIRouter, status
from ..schemas.vendedor_schema import Vendedor, VendedorCreate
from ..services.vendedor_service import vendedor_service

router = APIRouter(
    prefix="/vendendor",
    tags=["Vendedor"]
)

@router.post(
    "/",
    response_model=Vendedor,
    status_code=status.HTTP_201_CREATED
)
def registrar_vendendor(vendedor_data: VendedorCreate) -> Vendedor:
    vendedor = vendedor_service.cadastrar_vendendor(vendedor_data)
    return vendedor

@router.get(
    "/{id_vendedor}",
    response_model=Vendedor,
    status_code=200
)
def buscar_vendedor(id_vendedor: int) -> Vendedor :
    vendedor = vendedor_service.buscar_vendedor(id_vendedor)
    return vendedor