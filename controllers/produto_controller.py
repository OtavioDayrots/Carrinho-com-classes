from model.produto import Produto
import views.view_produto as view_produto

produtos = []

def cadastar_produto():
    nome = view_produto.nome_produto()

    qtd = view_produto.qtd_produto()

    produto = Produto(nome, qtd)

    produtos.append(produto)

def listar_produtos():
    view_produto.listar_produtos(produtos)

def incluir_no_estoque():
    produto = view_produto.selecionar_produto(produtos)

    if produto != None:
        qtd = view_produto.qtd_produto()

        produto.adicionar_produto(qtd)
