from ifood2.banco.db import conectar
from ifood2.models.cardapio.prato import Prato
from ifood2.models.cardapio.bebida import Bebidas

def tabela_item_cardapio():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_item_cardapio = """
        CREATE TABLE IF NOT EXISTS item_cardapio(
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_restaurante INT NOT NULL,
        nome_item VARCHAR(100) NOT NULL,
        preco FLOAT(6,2) NOT NULL,
        tipo_item VARCHAR(20) NOT NULL,
        descricao TEXT,
        tamanho VARCHAR(50),
        FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
    )
    """
    cursor.execute(criar_tabela_item_cardapio)
    conexao.commit()
    conexao.close()
    
def criar_item_cardapio(id_restaurante, nome_item, preco, tipo_item, descricao, tamanho):
    if isinstance(nome_item, Prato):
        tipo_item = "prato"
        descricao = nome_item.descricao
        tamanho = None
    elif isinstance(nome_item, Bebidas):
        tipo_item = "bebida"
        descricao = nome_item.descricao
        tamanho = None
    else:
        descricao = None
        tamanho = None


    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO item_cardapio(id_restaurante, nome_item, preco, tipo_item, descricao, tamanho)
        VALUES(%s, %s, %s, %s, %s, %s)
    """, (id_restaurante, nome_item, preco, tipo_item, descricao, tamanho))
    conexao.commit()
    conexao.close()