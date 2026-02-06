from fastapi import HTTPException, APIRouter, status
from schemas.vendendor_schema import Vendedor
from services.vendendor_service import VendendorService
router = APIRouter(
    prefix="/vendendor",
    tags=["Vendedor"]
)

@router.post(
    "/",
    response_model=Vendedor,
    status_code=status.HTTP_201_CREATED
)
def registrar_vendendor(id_pessoa,data_cadastro):
    vendedor = VendendorService()
    return vendedor.cadastrar_vendendor(id_pessoa, data_cadastro)