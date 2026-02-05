from schemas.produto_schema import Produto

produtos = []

class ProdutoRepository:

    def cadastrar_produto(nome_identificacao, preco, quantidade_estoque):
       produto = Produto(nome_identificacao, preco, quantidade_estoque)
       produtos.append(produto)
       return produto 