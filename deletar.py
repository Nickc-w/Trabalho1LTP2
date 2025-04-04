
from create import cursor,conexao
"""
    OBJETIVO:
    Deletar um produto da tabela pelo id, SEM RESETAR O ID
"""

def deletar_produto(id):
    
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))

    if cursor.rowcount > 0:
        conexao.commit()
        print("Produto deletado com sucesso!!")
      
    else:
        print("Produto nao encontrado!!")
