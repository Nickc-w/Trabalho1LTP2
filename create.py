""" 
OBJETIVO = 
Função de Criaçao do banco de dados e da tabela

"""

# Criando o Banco de dados
import sqlite3

global conexao,cursor
conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

def Criando():
    # Criando a tabela produtos
    cursor.execute(""" 
               
               CREATE TABLE IF NOT EXISTS produtos(
                    id integer primary key autoincrement,
                    nome text unique not null,
                    quantidade integer not null check(quantidade > 0),
                    preco real not null check(preco > 0) 
               )
    """)


    conexao.commit()




