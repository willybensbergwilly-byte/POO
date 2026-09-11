class Veiculos:
    
    def __init__(self, modelo, marca, ano,):
            self.modelo = modelo
            self.marca = marca
            self.ano = ano
            self._disponivel = False
            Veiculos.alterar_estado(self)
    
    
    def alterar_estado(self):
            self._disponivel = not self._disponivel 
            
    def __str__(self):
        return f"Modelo: {self.modelo} - Marca: {self.marca} - Ano: {self.ano} - Status: {str(self._status)}\n -------------------------------"
    @property
    def disponivel(self):
        return 'disponivel' if self._status else 'vendido'

veiculo1 = Veiculos("Civic", "Honda", 2020 )

veiculo2 = Veiculos("Corolla", "Toyota", 2021)

veiculo3 = Veiculos("Gol", "Volkswagen", 2019)

veiculo4 = Veiculos("Uno", "Fiat", 2018)

veiculo5 = Veiculos("Ka", "Ford", 2020)

veiculo6 = Veiculos("Onix", "Chevrolet", 2021)


print(veiculo1)    
print(veiculo2)    
print(veiculo3)    
print(veiculo4)    
print(veiculo5)    
print(veiculo6)    