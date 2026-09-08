class Produto:
    def __init__(self, nome, preco):
            self.nome = nome
            self.preco = preco
            self.ativo = False
            
produto01 = Produto("detergente, 12.99")
print(produto01.nome)
print(produto01.preco)

