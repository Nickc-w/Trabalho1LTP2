
from create import cursor
"""
    OBJETIVO:
    Listar todos os produtos

"""

def listar_produtos():
    cursor.execute("SELECT * FROM produtos") 
    itens = cursor.fetchall()
    for i in itens:
        # i = (id,nome,quantidade,preço)
        print(f"id: {i[0]}, Nome: {i[1]}, Quantidade: {i[2]}, Preço: {i[3]}")

    


              
