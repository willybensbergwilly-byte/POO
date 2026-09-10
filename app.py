from  models.restaurantes import Restaurante

la_mafia = Restaurante("La Mafia", "Rua das Flores, 123", "Comida Italiana", 15)
mada = Restaurante("Mada", "Rua das Palmeiras, 456", "Comida Brasileira", 20)
steve_pizza = Restaurante("Steve Pizza", "Rua das Laranjeiras, 789", "Comida Japonesa", 10)
Restaurante.alterar_estado(la_mafia)

la_mafia.receber_avaliacoes("Noreh", 5)

def main():
    Restaurante.listar_restaurante()
    
if __name__ == '__main__':
    main()
