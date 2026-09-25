from models.cardapio.itemcardapio import ItemCardapio
class Bebidas(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho