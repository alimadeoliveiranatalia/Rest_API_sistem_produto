from ..schemas.produto_schema import ProdutoCreate
from ..repositories.produto_repository import produto_repository

class ProdutoService:
    def __init__(self):
        self.produto = produto_repository

    def cadastrar_produto(self, produto_data: ProdutoCreate):
        """Regra de negócio para cadastrar o produto."""
        produto = self.produto.cadastrar_produto(produto_data)
        return produto
    
    def buscar_produto(self, produto_id):
        """Regra de Negócio para buscar um produto passando seu ID."""
        produto = self.produto.buscar_produto(produto_id)
        return produto
    
produto_service = ProdutoService()