from fastapi import HTTPException, APIRouter, status
from schemas.vendendor_schema import Vendedor, VendendorCreate
from services.vendendor_service import vendedor_service
router = APIRouter(
    prefix="/vendendor",
    tags=["Vendedor"]
)

@router.post(
    "/",
    response_model=Vendedor,
    status_code=status.HTTP_201_CREATED
)
def registrar_vendendor(vendedor_data: VendendorCreate) -> Vendedor:
    vendedor = vendedor_service.cadastrar_vendendor(vendedor_data)
    return vendedor

@router.get(
    "/{id_vendedor}",
    response_model=Vendedor,
    status_code=200
)
def buscar_vendedor(id_vendedor) -> Vendedor :
    return vendedor_service.buscar_vendedor(id_vendedor)