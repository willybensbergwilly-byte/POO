import mysql.connector
def conectar():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="~~WrbdskmNN777",
    database="ifood2"
    )
    return conexao

    

