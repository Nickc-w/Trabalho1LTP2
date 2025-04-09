from insert import CriarProduto
from listar import listar_produtos
from Atualizar import Atualizar
from deletar import deletar_produto
from create import conexao



""" OBJETIVO:
    Criar o menu com as opçoes de criar produto, listar produtos, atualizar produto e deletar produto
"""



from FuncoesVerificaçaoTipos import ConferirTipoInt,ConferirTipoFloat


def menu():
    while True:  
        print("\n                  BEM VINDO ;) ")
        print("\n    ----------ESTOQUE DE PRODUTOS-------------\n")
        print("     [1] Criar um novo produto no estoque.\n"
              "     [2] Listar todos os produtos disponíveis.\n"
              "     [3] Atualizar a quantidade e o preço de um produto existente.\n"
              "     [4] Deletar um produto pelo ID\n"
              "     [5] Sair\n")

        try:
            opcao = int(input("Digite sua opção: "))  # Tenta pegar a opção do usuário
        except ValueError:
            print("Digite um tipo válido! ")
            continue  # Se houver erro (não for int), repete o laço sem chamar a função menu() novamente

        if opcao == 5:
            print("\nObrigada!\n")
            conexao.close()  # Fecha a conexão com o banco de dados antes de sair
            break  # Sai do laço e termina o programa

        elif opcao == 1: # Criar
            nome = input("Informe o nome do produto: ").strip().lower()
            if not nome == '':
                CriarProduto(nome, ConferirTipoInt("Informe a quantidade do produto: "), ConferirTipoFloat("Informe o preço do produto: "))
            else:
                print("Informe um nome para o produto!")

        elif opcao == 2: # Listar
            listar_produtos()
        
        elif opcao == 3: # Atualizar
            Atualizar(ConferirTipoInt("Informe o [id] do produto que quer atualizar: "), 
                      ConferirTipoInt("Informe a nova quantidade do produto que quer atualizar: "), 
                      ConferirTipoFloat("Informe o novo preço do produto que quer atualizar: "))
        
        elif opcao == 4: # Deletar
            deletar_produto(ConferirTipoInt("Informe o id do produto que deseja deletar: "))
        
        else:
            print("Digite uma opção válida! ") # Se for um numero que não esteja nas opções disponíveis (1,2,3,4,5)
       
