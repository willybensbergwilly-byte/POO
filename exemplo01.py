class Restaurante:
    restaurantes = []  
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        # return self.nome
        return f"{self.nome}, nossa especialidade é comida {self.categoria}"
    def listar_restaurantes(self):
        for restaurante in Restaurante.restaurantes:
            print(f'Restaurante: {restaurante.nome}, Categoria: {restaurante.categoria}')
 
nome_restaurante = input("Digite o nome do restaurate: ")
categoria_restaurante = input("Digite a categoria do restaurate: ")
mada = Restaurante(nome_restaurante, categoria_restaurante)
restaurantes_01 = Restaurante ("Mada","italiana") 
restaurantes_02 = Restaurante  ("Braseirinho", "Brasileira")
restaurantes = [restaurantes_01, restaurantes_02]

print(restaurantes_01, restaurantes_02)
print(restaurantes)

