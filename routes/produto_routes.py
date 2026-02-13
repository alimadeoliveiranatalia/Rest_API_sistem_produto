from fastapi import HTTPException, APIRouter, status
from ..services.produto_service import produto_service
from ..schemas.produto_schema import Produto, ProdutoCreate

router = APIRouter(
    prefix="/produto",
    tags=["Produto"]
)

@router.post(
    "/",
    response_model=Produto,
    status_code=status.HTTP_201_CREATED
)
def registrar_produto(produto_data: ProdutoCreate) -> Produto:
    produto = produto_service.cadastrar_produto(produto_data)
    return produto

@router.get(
    "/{id_produto}",
    response_model=Produto,
    status_code=200
)
def buscar_produto(id_produto: int) -> Produto:
    produto = produto_service.buscar_produto(id_produto)
    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não Encontrado"
        )
    return produto