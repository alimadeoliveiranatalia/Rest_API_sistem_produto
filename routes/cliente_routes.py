from fastapi import HTTPException, APIRouter, status
from ..schemas.cliente_schema import ClienteCreate, Cliente
from ..services.cliente_service import cliente_service

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.post(
    "/",
    response_model=Cliente,
    status_code=status.HTTP_201_CREATED
)
def registrar_cliente(cliente_data: ClienteCreate) -> Cliente:
    return cliente_service.efetuar_cadastro_cliente(cliente_data)