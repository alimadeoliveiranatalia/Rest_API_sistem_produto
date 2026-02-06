from fastapi import HTTPException, APIRouter, status
from .schemas.cliente_schema import Cliente
from services.cliente_service import ClienteService

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.post(
    "/",
    response_model=Cliente,
    status_code=status.HTTP_201_CREATED
)
def registrar_cliente(id_pessoa, dataCadastro):
    cliente = ClienteService()
    return cliente.efetuar_cadastro_cliente(id_pessoa, dataCadastro)