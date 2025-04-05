
from create import cursor,conexao,sqlite3
"""
    OBEJTIVO:
        Atualizar a quantidade e o preço de um produto pelo [id]

"""

def Atualizar(id,nova_quantidade,novo_preco):

    try:
        cursor.execute("UPDATE produtos SET quantidade = ?, preco = ? WHERE id = ?", (nova_quantidade,novo_preco,id))

        
        if cursor.rowcount > 0:
            conexao.commit()
            print("Quantidade e preço atualizados com sucesso!")
        else:
            print("Item não encontrado! Atualizaçao nao realizada") # se não encontrar o produto
            
    except sqlite3.IntegrityError as e:
        print(f"Produto nao atualizado. Erro de integridade!! = {e}") # Se a quantidade ou preço forem negativos
    



