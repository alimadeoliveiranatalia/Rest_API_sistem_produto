from repositories.produto_repository import ProdutoRepository

class ProdutoService:
    def cadastrar_produto(nome_identificacao, preco, quantidade_estoque):
        produto = ProdutoRepository()
        return produto.cadastrar_produto(nome_identificacao, preco, quantidade_estoque)