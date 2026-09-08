class Produto:
    def __init__(self, nome, preco):
            self.nome = nome
            self.preco = preco
            self.ativo = False
            
produto01 = Produto("detergente, 12.99")
print(produto01.nome)
print(produto01.preco)

produto01 = Produto("Detergente", 12.99)
produto02 = Produto("Quiboa", 17.99)
produto03 = Produto("Desinfetante", 42.99)

print(produto01)
print(produto02)
print(produto03)

