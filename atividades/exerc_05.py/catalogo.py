class Filmes:
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        
        def __str__(self):
           return f"|titulo:{self.titulo}\n | genero:{self.genero}\n| ano:{ano}|"