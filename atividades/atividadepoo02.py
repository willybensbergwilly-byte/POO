class Restaurante:
    def __init__(self, nome, localizacao, tipo_de_comida, quantidade_funcionarios):
            self.nome_restaurante = nome
            self.localizacao = localizacao
            self.tipo_de_comida = tipo_de_comida
            self.quantidade_funcionarios = quantidade_funcionarios
            self.ativo = False

    def __str__(self):
        return f"Nome: {self.nome_restaurante}\n - Rua: {self.localizacao}\n Tipo de Comida: {self.tipo_de_comida}\n - Quantidade de Funcionários: {str(self.quantidade_funcionarios)}"
    
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f"Nome: {restaurante.nome_restaurante} \n|Rua: {restaurante.localizacao} \n|Tipo de Comida: {restaurante.tipo_de_comida} \n|Quantidade de Funcionários: {str(restaurante.quantidade_funcionarios)} \n|Status: {restaurante.status}")
 
la_mafia = Restaurante("La Mafia", "Rua das Flores, 123", "Comida Italiana", 15)
mada = Restaurante("Mada", "Rua das Palmeiras, 456", "Comida Brasileira", 20)
steve_pizza = Restaurante("Steve Pizza", "Rua das Laranjeiras, 789", "Comida Japonesa", 10)

Restaurante.listar_restaurante()
      






