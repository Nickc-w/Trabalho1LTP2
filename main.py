from menu import menu
from create import Criando



""" 
    OBEJTIVO:
    Executar o codigo (criando o BD e a tabela quando executar o codigo!!), chamando menu e fazer testes
"""



Criando()
menu()



''' Testes (mesmo dos que estão no READ ME do github"

-> Menu (1,2,3,4 ou 5)

# certo
Digite sua opção: 3

# erro (opção fora das opções)
Digite sua opção: 7

# erro (tipo errado)
Digite sua opção: idjfe


-> Criar
# 1 - certo
Informe o nome do produto: Banana 
Informe a quantidade do produto: 100 
Informe o preço do produto:  6.7 

#2 - erro (tipo errado)
Informe o nome do produto: Banana  
Informe a quantidade do produto: lalala (string)  
Informe o preço do produto:  lalala (string) 

# 3 erro
Informe o nome do produto: Banana # que ja existe! 
Informe a quantidade do produto: 50 
Informe o preço do produto:  3.5 

# 4 - erro
Informe o nome do produto: Maça  
Informe a quantidade do produto: 50 
Informe o preço do produto:  -3.5 (negativo)

 4 - erro
Informe o nome do produto:      (precisa de um nome)
Informe a quantidade do produto: 50 
Informe o preço do produto:  3.4 


-> Atualizar
#5 - certo
Informe o [id] do produto que quer atualizar: 1 
Informe a nova quantidade do produto que quer atualizar: 50 
Informe o novo preço do produto que quer atualizar: 3.5 

#6 - erro (tipo errado)
Informe o [id] do produto que quer atualizar: wwef 
Informe a nova quantidade do produto que quer atualizar: kscl 
Informe o novo preço do produto que quer atualizar: iojsxaij 


#7 - erro
Informe o [id] do produto que quer atualizar: 5 (id não existe)
Informe a nova quantidade do produto que quer atualizar: 50 
Informe o novo preço do produto que quer atualizar: 2.3 

#8 - erro 
Informe o [id] do produto que quer atualizar: 1 
Informe a nova quantidade do produto que quer atualizar: -50 (negativo)
Informe o novo preço do produto que quer atualizar: 2.3 


-> Deletar
#9 - certo
Informe o id do produto que deseja deletar: 1 

#10 - erro (id não existe)
Informe o id do produto que deseja deletar: 5 


'''







 


