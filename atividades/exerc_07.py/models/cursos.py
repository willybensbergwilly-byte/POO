from models.aluno import Aluno
class Curso:
    cursos = []
    def __init__(self, nome_curso):
        self.nome_curso = nome_curso
        self._alunos = []
        Curso.cursos.append(self)

    def matricular_aluno(self, nome, idade):
        aluno = Aluno(nome, idade)
        self._alunos.append(aluno)

    def listar_alunos(self):
        print(f"{self.nome_curso}")
        for aluno in self._alunos:
            print(f"Nome Aluno: {aluno._nome.ljust(20)}|Idade: {aluno._idade}")
    
 