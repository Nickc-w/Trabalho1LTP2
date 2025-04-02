
from create import conexao,cursor,sqlite3 # só importar quando necessário

""" 
    OBJETIVO :
    Criar novos produtos no estoque = inserir um produto na tabela Produtos = insert into

"""

# Funçao para criar um novo produto no estoque 
def CriarProduto(nome,quantidade,preco):
    try:
        cursor.execute("INSERT INTO produtos(nome,quantidade,preco) VALUES(?,?,?)",(nome,quantidade,preco))
        conexao.commit() # salva
        print(f"Produto inserido ao estoque com sucesso!! ID: {cursor.lastrowid}")
    except sqlite3.IntegrityError as e:
        print(f"Produto nao inserido. Erro de integridade!! = {e}") # Para evitar duplicidade,...etc


    




