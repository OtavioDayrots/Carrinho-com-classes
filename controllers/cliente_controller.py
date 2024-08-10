from model.cliente import Cliente
import controllers.produto_controller
import views.view_cliente as view_cliente
import views.view_produto as view_produto

clientes = []

def cadastrar():
    nome = view_cliente.nome_cliente()

    cliente1 = (Cliente(nome))

    clientes.append(cliente1)

def deletar():
    selecionado = view_cliente.selecionar_cliente(clientes)
    
    if selecionado != None:
        clientes.pop(selecionado)

def editar():
    selecionado = view_cliente.selecionar_cliente(clientes)
    if selecionado != None:
        cliente = view_cliente.editando_cliente(clientes[selecionado])

        clientes[selecionado] = cliente

def listar():
    view_cliente.listar_clientes(clientes)


def adicionar_ao_carrinho():
    selecionado = view_cliente.selecionar_cliente(clientes)
    
    if selecionado != None:
        produto = view_produto.selecionar_produto(controllers.produto_controller.produtos)

        if produto != None:
            qtd = view_cliente.qtd_produto()

            clientes[selecionado].adicionar_produto(produto, qtd)

def excluir_do_carrinho():
    selecionado = view_cliente.selecionar_cliente(clientes)
    
    if selecionado != None:
       produto = view_cliente.selecionar_produto(clientes[selecionado].carrinho.get_lista_produto())

       clientes[selecionado].carrinho.remover_do_carrinho(produto)

def listar_carrinho():
    selecionado = view_cliente.selecionar_cliente(clientes)

    if selecionado != None:
        view_cliente.listar_carrinho(clientes[selecionado])
