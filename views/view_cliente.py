def exibir_cliente(cliente):
    print('-' * 60)
    print(f'Cliente - (Nome: {cliente.nome})')

def listar_clientes(lista):
    for cliente in lista:
        exibir_cliente(cliente)

def menu_principal():
    print('Menu Principal'.center(60, '-'))
    print(
        '[1] Menu do Cliente\n'
        '[2] Menu Produto\n'
        '[0] Sair do programa'
        )
    
    try:
        controle = int(input('Escolha uma opção: '))
    
    except(TypeError):
        print('Erro de tipo')

    except(KeyboardInterrupt):
        pass

    return controle

def menu_do_cliente():
    print('Menu do Cliente'.center(60, '-'))
    print(
        '[1] Cadastrar cliente\n'
        '[2] Excluir cliente\n'
        '[3] Listar clientes\n'
        '[4] Editar cliente\n'
        '[5] Adicionar ao carrinho\n'
        '[6] Excluir da lista\n'
        '[7] Listar Carrinho\n'
        '[0] Sair do menu do cliente'
        )
    
    try:
        controle = int(input('Escolha uma opção: '))
    
    except(TypeError):
        print('Erro de tipo')

    except(KeyboardInterrupt):
        pass

    return controle

def nome_cliente():
    nome = input('Infome o nome do cliente: ')

    return nome

def selecionar_cliente(lista):
    nome = nome_cliente()

    for cliente in lista:
        if cliente.nome == nome:
            index = lista.index(cliente)

            print(f'Cliente {nome} encontrado')
            return index
    
    print('Cliente não encontrado')
    
    return None

def nome_produto():
    nome = input('Informe o nome do produto: ')

    return nome

def qtd_produto():
    qtd = int(input('Informe o quantidade do produto: '))

    return qtd

def selecionar_produto(lista):
    nome = nome_produto()

    for produto in lista:
        if produto.get_nome() == nome:

            print(f'Produto {nome} encontrado')
            return produto
    
    print('Produto não encontrado')
    
    return None

def editando_cliente(cliente):
    cliente_editado = cliente

    cliente_editado.nome = input(f'Informe o novo nome do cliente {cliente_editado.nome}: ')

    return cliente_editado

def encerrar():
    print('Saindo...')

def erro():
    print('opção invalida!')

def exibir_produto_carrinho(produto):
    print('-'*60)
    print('Produto'.center(60))
    print(f'Nome do produto: {produto.get_nome()}')
    print(f'Tem {produto.get_quantidade()}')

def listar_carrinho(cliente):
    carrinho = cliente.carrinho

    print('-'*60)
    print(f'Carrinho do cliente {cliente.nome}'.center(60))

    for produto in carrinho.get_lista_produto():
        exibir_produto_carrinho(produto)
    print('-'*60)
