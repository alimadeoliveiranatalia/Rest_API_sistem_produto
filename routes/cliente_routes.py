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

@router.get(
    "/{id_cliente}",
    response_model=Cliente,
    status_code=200
)
def buscar_cliente_por_id(id_cliente: int) -> Cliente:
    cliente = cliente_service.buscar_cliente(id_cliente)
    if not cliente:
        raise HTTPException(
            status_code=400,
            detail="Cliente não encontrado"
        )
    return cliente