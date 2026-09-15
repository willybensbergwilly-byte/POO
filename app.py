from models.restaurantes import Restaurante
from models.cardapio.bebida import Bebidas
from models.cardapio.prato import Prato
la_mafia = Restaurante("La Mafia", "Rua das Flores, 123", "Comida Italiana", 15)
mada = Restaurante("Mada", "Rua das Palmeiras, 456", "Comida Brasileira", 20)
steve_pizza = Restaurante("Steve Pizza", "Rua das Laranjeiras, 789", "Comida Japonesa", 10)
Restaurante.alterar_estado(la_mafia)

la_mafia.receber_avaliacoes("Noreh", 5)

pastel = Prato("pastel de rato", 6.66, "Pastel de rato shodebola")
leitededemiurgo = Bebidas("lentinho de demiurgo docinho docinho", 4.99, "400ml")

la_mafia.adicionar_cardapio(pastel)
la_mafia.adicionar_cardapio(leitededemiurgo)


def main():
    Restaurante.listar_restaurante()    
    print(pastel)
    print(leitededemiurgo)

def main():
        la_mafia.exibir_cardapio
    
if __name__ == '__main__':
    main()
