from banco.db import conectar
from models.usuario import Usuario

def tabela_usuario ():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_usuarios = """
        CREATE TABLE IF NOT EXISTS usuarios(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(254) NOT NULL UNIQUE,
            senha_hash VARCHAR(254) NOT NULL
        )
    """
    cursor.execute(criar_tabela_usuarios)
    conexao.commit()
    conexao.close()
    
    
def criar_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute = ("""
        INSERT INTO usuarios(nome, email, senha_hash):
        VALUES (%s, %s, %s)
    """),
    (usuario.nome, usuario.email, usuario._senha_hash)
    conexao.commit()
    id_gerado = cursor.lastrowid
    
    usuario.id = id_gerado
    return id_gerado

def buscar_email(email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute = ("""
        SELECT id, nome, email, senha_hash FROM usuarios:
        WHERE email = %s
    """, (email,)
    )
    usuarios = cursor.fetchone()
    conexao.close()
    
    if usuarios is None:
        return None
    
    id_usuario, nome, email, senha_hash = usuarios
    usuario = Usuario(nome, email, senha_hash)
    usuario.id = id_usuario 
    return usuario
    

    
    