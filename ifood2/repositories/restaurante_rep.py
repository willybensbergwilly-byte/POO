from banco.db import conectar
from models.restaurantes import Restaurante


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


def buscar_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT id, nome, categoria, ativo FROM restaurantes
    WHERE id = %s
    """, (id,))
    restaurante = cursor.fetchone()
    conexao.close()
    
    if restaurante is None:
        return None
    id_banco, nome, categoria, ativo = restaurante
    restaurante = Restaurante(nome,categoria)
    restaurante._ativo = bool(ativo)
    restaurante.id = id_banco
    return restaurante

def listar_completo(id):
    from repositories import cardapio_rep, avaliacoes_rep
    restaurante = buscar_por_id(id)
    if restaurante is None:
        return None
    else:
        for avaliacao in avaliacoes_rep.listar_avaliacoes(id):
            restaurante._avaliacoes.append(avaliacao)
            for item in cardapio_rep.listar_por_restaurante(id):
                restaurante._cardapio.append(item)
                return restaurante