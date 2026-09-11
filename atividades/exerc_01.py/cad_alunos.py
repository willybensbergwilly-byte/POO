class Aluno:
 
    # Método construtor
    def __init__(self, nome, curso, idade):
        self.nome = nome
        self.curso = curso
        self.idade = idade
 
    # Define como o objeto será exibido no print()
    def __str__(self):
        return f"| Nome: {self.nome}\n| Curso: {self.curso}\n| Idade: {self.idade} anos\n"
 
# Criando os três objetos
aluno1 = Aluno("João", "Progamador de Sistemas", 18)
aluno2 = Aluno("Maria", "Programador Web", 20)
aluno3 = Aluno("Carlos", "Técnico em Informática", 17)
 
# Exibindo os alunos
print(aluno1)
print(aluno2)
print(aluno3)