from banco.db import conectar
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida


def tabela_item_cardapio():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_item_cardapio = """
        CREATE TABLE IF NOT EXISTS item_cardapio(
            id INT PRIMARY KEY AUTO_INCREMENT,
            id_restaurante INT NOT NULL,
            nome VARCHAR(100) NOT NULL,
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

def criar_item_cardapio(id_restaurante, item):
    if isinstance(item, Prato): 
        tipo_item = 'Prato'
        descricao = item.descricao
        tamanho = None
    elif isinstance(item, Bebida): 
        tipo_item = 'Bebida'
        descricao = None
        tamanho = item.tamanho

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO item_cardapio(id_restaurante, nome, preco, tipo_item, descricao, tamanho) 
        VALUES (%s, %s, %s, %s, %s, %s) 
        """, (id_restaurante, item._nome, item._preco, tipo_item, descricao, tamanho)
    )
    conexao.commit()
    conexao.close()

def listar_por_restaurante(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM item_cardapio WHERE id_restaurante = %s", (id,))
    resultado = cursor.fetchall()
    conexao.close()
    # Aqui que muda esse caraio
    itens = []
    for nome, preco, tipo_item, descricao, tamanho in resultado:
        preco_item = float(preco)
        if tipo_item == 'prato':
            itens.append(Prato(nome, preco_item, descricao))
        elif tipo_item == 'bebida':
            itens.append(Bebida(nome, preco_item, tamanho))
    return itens