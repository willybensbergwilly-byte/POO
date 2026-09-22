import mysql.connector
def conectar():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="~~WrbdskmNN777",
    database="ifood2"
    )
    return conexao



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
        """, (nome, categoria))
    conexao.commit()
    conexao.close()


    
def listar_restaurantes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM restaurantes                       
    """)
    restaurantes = cursor.fetchall()
    for restaurante in restaurantes:
        print(restaurante)
    conexao.commit()
    conexao.close()



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
    """, (nome_usuario, nota, id_restaurante))
    conexao.commit()
    conexao.close()
    
    
    
def listar_avaliacoes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT restaurantes.nome_restaurante, avaliacoes.nome_usuario, avaliacoes.nota FROM
    avaliacoes JOIN restaurantes ON avaliacoes.id_restaurante = restaurante.id
    """)
    avaliacoes = cursor.fetchall()
    for avaliacoes in avaliacoes:
        print(avaliacoes)
    conexao.commit()
    conexao.close()
    
    
    
def tabela_item_cardapio():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_item_cardapio = """
    CREATE TABLE IF NOT EXISTS item_cardapio(
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_restaurante INT NOT NULL,
        nome_item VARCHAR(100) NOT NULL,
        preco FLOAT(6,2) NOT NULL,
        FOREIGN KEY (id_restaurante) REFERENCES restaurante(id)
    )
    """
    cursor.execute(criar_tabela_item_cardapio)
    conexao.commit()
    conexao.close()