# from venv.models.restaurantes import Restaurante
# from venv.models.cardapio.bebida import Bebidas
# from venv.models.cardapio.prato import Prato
# la_mafia = Restaurante("La Mafia", "Rua das Flores, 123", "Comida Italiana", 15)
# mada = Restaurante("Mada", "Rua das Palmeiras, 456", "Comida Brasileira", 20)
# steve_pizza = Restaurante("Steve Pizza", "Rua das Laranjeiras, 789", "Comida Japonesa", 10)
# Restaurante.alterar_estado(la_mafia)

# la_mafia.receber_avaliacoes("Noreh", 5)

# pastel = Prato("pastel de rato", 6.66, "Pastel de rato shodebola")
# leitededemiurgo = Bebidas("lentinho de demiurgo docinho docinho", 4.99, "400ml")

# la_mafia.adicionar_cardapio(pastel)
# la_mafia.adicionar_cardapio(leitededemiurgo)


# def main():
#     Restaurante.listar_restaurante()    
#     print(pastel)
#     print(leitededemiurgo)

# def main():
#         la_mafia.exibir_cardapio
    
# if __name__ == '__main__':
#     main()

from repositories.cardapio_rep import tabela_item_cardapio, criar_item_cardapio
from ifood2.banco.db import tabela_restaurante, criar_restaurante, listar_restaurantes, tabela_avaliacoes, criar_avaliacoes

def main():
    tabela_item_cardapio()
    criar_item_cardapio()
    # criar_restaurante("Green Dog", "HotDog")
    # criar_avaliacoes("1","Não é o Heron", 4.5)

if __name__ == '__main__':
    main()
    

tabela_restaurante()
tabela_avaliacoes()
tabela_item_cardapio()


criar_restaurante("Green Dog", "HotDog")
criar_avaliacoes("1","Não é o Heron", 4.5)

listar_restaurantes()