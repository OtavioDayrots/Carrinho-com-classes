from model.cliente import Cliente
from model.produto import Produto
import controllers.cliente_controller
import controllers.produto_controller
import views.view_cliente as view_cliente
import views.view_produto as view_produto

def menu_cliente():

    while True:

        op_cliente = -1

        op_cliente = view_cliente.menu_do_cliente()

        if op_cliente == 1:
            controllers.cliente_controller.cadastrar()

        elif op_cliente == 2:
            controllers.cliente_controller.deletar()
        
        elif op_cliente == 3:
            controllers.cliente_controller.listar()
        
        elif op_cliente == 4:
            controllers.cliente_controller.editar()

        elif op_cliente == 5:
            controllers.cliente_controller.adicionar_ao_carrinho()

        elif op_cliente == 6:
            controllers.cliente_controller.excluir_do_carrinho()

        elif op_cliente == 7:
            controllers.cliente_controller.listar_carrinho()

        elif op_cliente == 0:
            view_cliente.encerrar()

            break

        else:
            view_cliente.erro()

def menu_produto():
    op_produto = ''
    while True:
        op = view_produto.menu_produto()

        match op:
            case 1:
                controllers.produto_controller.cadastar_produto()

            case 2:
                controllers.produto_controller.listar_produtos()

            case 3:
                controllers.produto_controller.incluir_no_estoque()

            case 0:
                break

            case _:
                view_produto.erro()

try:

    op = ''

    while True:
        op = view_cliente.menu_principal()
        match op:
            case 1: 
                menu_cliente()

            case 2:
                menu_produto()

except(UnboundLocalError, KeyboardInterrupt):
    print('O Usuário decidiu encerrar o programa')


# clientes = []
# produtos = []

# cliente1 = Cliente('Otávio Bonito')
# cliente2 = Cliente('Luiz')
# cliente3 = Cliente('Matheus')

# clientes.append(cliente1)
# clientes.append(cliente2)
# clientes.append(cliente3)

# view.listar_clientes(clientes)

# produto1 = Produto('arroz', 15)
# produto2 = Produto('feijão', 20)
# produto3 = Produto('abacaxi', 40)
# produto4 = Produto('abobora',20)

# produtos.append(produto1)
# produtos.append(produto2)
# produtos.append(produto3)
# produtos.append(produto4)

# view.listar_produtos(produtos)

# print('\n\n\n\n')

# cliente1.adicionar_produto(produto4, 3)

# view.listar_carrinho(cliente1)

# print('\n')

# cliente2.adicionar_produto(produto4, 2)

# view.listar_carrinho(cliente2)

# print('\n')

# cliente3.adicionar_produto(produto4, 4)

# view.listar_carrinho(cliente3)

