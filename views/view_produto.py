def exibir_produto(produto):
    print('-'*60)
    print('Produto'.center(60))
    print(f'Nome do produto: {produto.get_nome()}')
    print(f'Quantidade do estoque: {produto.get_quantidade()}')

def listar_produtos(lista):
    for produto in lista:
        exibir_produto(produto)

def menu_produto():
    print('Menu do produto'.center(60, '-'))
    print(
        '[1] Cadastrar produto\n'
        '[2] Listar produtos\n'
        '[3] Incluir produto\n'
        '[0] Sair do menu do produto'
        )
    
    try:
        controle = int(input('Escolha uma opção: '))
    
    except(TypeError):
        print('Erro de tipo')

    except(KeyboardInterrupt):
        pass

    return controle

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

def erro():
    print('opção invalida!')