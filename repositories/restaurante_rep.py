from ifood2.banco.db import conectar
from ifood2.models.restaurantes import Restaurante


def tabela_restaurante ():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_restaurantes = """
        CREATE TABLE IF NOT EXISTS restaurantes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            categoria VARCHAR(45) NOT NULL,
            ativo BOOLEAN DEFAULT FALSE NOT NULL
            )
        """
    cursor.execute(criar_tabela_restaurantes)
    conexao.commit()
    conexao.close()
    
    
def criar_restaurante(nome, categoria):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(""" 
    INSERT INTO restaurantes(nome, categoria)
    VALUES(%s, %s)              
    """, (listar_restaurantes.nome, listar_restaurantes.categoria))
    conexao.commit()
    conexao.close()


def listar_restaurantes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM restaurantes                       
    """)
    restaurantes = cursor.fetchall()
    conexao.commit()
    conexao.close()
    return  [Restaurante(nome,categoria) for nome,categoria in restaurantes]

