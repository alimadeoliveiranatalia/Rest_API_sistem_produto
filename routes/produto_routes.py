from fastapi import HTTPException, APIRouter, status
from services.produto_service import ProdutoService
from schemas.produto_schema import Produto

router = APIRouter(
    prefix="/produto",
    tags=["Produto"]
)

@router.post(
    response_model=Produto,
    status_code=status.HTTP_201_CREATED
)
def registrar_produto(nome_descricao, preco, quantidade_estoque):
    produto = ProdutoService()
    return produto.cadastrar_produto(nome_descricao,preco, quantidade_estoque)