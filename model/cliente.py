from model.carrinho import Carrinho

class Cliente:
    def __init__(self, nome: str):
        self.nome = nome

        self.carrinho = Carrinho()

    def exibir_nome(self):
        print(f'nome: {self.nome}.')

    def adicionar_produto(self, produto, quantidade):
        self.carrinho.adicionar_ao_carrinho(produto, quantidade)

