from model.produto import Produto

class Carrinho:
    def __init__(self):
        self.__lista_produto = []

    def adicionar_ao_carrinho(self, produto, quantidade):
        # validar a quantidade que o cliente vai adicionar ao carrinho
        if quantidade > 0:

            # validar quantidade em estoque
            if produto.possui_quantidade_disponivel(quantidade):
                nome = produto.get_nome()

                produto_cliente = Produto(nome, quantidade)

                self.__lista_produto.append(produto_cliente)

                produto.debitar_quantidade(quantidade)

            else:
                raise Exception ('Quantidade indisponivel em estoque!')

        else:
            raise Exception('Quantidade selecionada inválida!')
        
    def remover_do_carrinho(self, produto):
        for pro in self.__lista_produto:
            if produto.get_nome() == pro.get_nome():

                index = self.__lista_produto.index(pro)

                self.__lista_produto.pop(index)

                print(f'Produto {produto.get_nome()} encontrado e removido')
        
        print('Produto não encontrado')
        
    def get_lista_produto(self):
        return self.__lista_produto

