from models.cursos import Curso

sistemas = Curso("Desenvolvedor de sistemas")
web = Curso("Desenvolvedor web")

sistemas.matricular_aluno("Paulo", 18)
sistemas.matricular_aluno("Willy", 20)
sistemas.matricular_aluno("Paulo", 18)

web.matricular_aluno("Darion", 45)
web.matricular_aluno("Pietro", 17)
web.matricular_aluno("Siwana", 24)

def main():
    Curso.listar_alunos(web)
    
if __name__ == '__main__':
    main()