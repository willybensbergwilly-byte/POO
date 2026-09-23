from ifood2.banco.db import conectar

def tabela_avaliacoes ():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_avaliacoes = """
        CREATE TABLE IF NOT EXISTS avaliacoes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_usuario VARCHAR(100) NOT NULL,
            nota FLOAT(2,1) NOT NULL,
            id_restaurante INT NOT NULL,
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
            )
        """
    cursor.execute(criar_avaliacoes)
    conexao.commit()
    conexao.close()
    
    
    
    
def criar_avaliacoes(nome_usuario, nota, id_restaurante):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO avaliacoes(nome_usuario, nota, id_restaurante)
        VALUES(%s, %s, %s)
    """, (nome_usuario,  nota, id_restaurante))
    conexao.commit()
    conexao.close()
    
    
    
        
def listar_avaliacoes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT restaurantes.nome_restaurante, avaliacoes.nome_usuario, avaliacoes.nota FROM
    avaliacoes JOIN restaurantes ON avaliacoes.id_restaurante = restaurantes.id
    """)
    Avaliacoes = cursor.fetchall()
    for avaliacoes in Avaliacoes:
        print(avaliacoes)
    conexao.commit()
    conexao.close()
    return  [Avaliacoes(cliente, nota) for cliente, nota in Avaliacoes]