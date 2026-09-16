class Livro:
    livros = []
    def __init__(self, autor, nome, data, disponivel):
        self.nome = nome
        self.autor = autor
        self.data = data
        self.disponivel = True
        Livro.livros.append(self)
                
        def __str__(self):
            return f"|Titulo:{self.titulo}\n    |Autor:{self.autor}\n   |Data:{self.data}\n    |Disponivel:{self.disponivel}\n"
        @property
        def disponibilidade(self):
            return "Disponível" if self.disponivel else "Emprestado"
        
        def emprestar(self):
            if self.disponivel == False:
                self.disponivel = True
            else:
                  return 
            livro1 = Livro("1984", "George Orwell", "08/07/1949", True)
    