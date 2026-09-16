class Funcionario:
    funcionarios = []
    
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario
        
        Funcionario.funcionarios.append(self)
        
    def __str__(self):
            return f"Nome funcionario: {self.nome} \n | Cargo do Funcionario: {self.cargo}\n | salario {self.salario}"
        
    @property
    def cambio_salario(self):
        return f"R${(self._salario,2)}"
    
    def aumentar_salario(self, percentual):
        
            calculo_percentual = percentual / 100
            aumento = self._salario = calculo_percentual
            self._salario = self._salario + aumento
            
paulo = Funcionario("Paulo", "Repositor", 2500)
    
Funcionario.aumento_salario(paulo,15)
    
print(paulo)