# 📦 Gerenciamento de Estoque com SQLite

Este é um sistema simples para gerenciar um pequeno estoque de produtos utilizando um banco de dados SQLite.

## 🚀 Funcionalidades

O sistema permite realizar operações básicas de CRUD (Create, Read, Update, Delete) no banco de dados.

### 📌 Estrutura do Banco de Dados

A tabela **`produtos`** contém os seguintes campos:

- `id` → Chave primária (auto incremento)
- `nome` → Texto (único e obrigatório)
- `quantidade` → Inteiro (obrigatório e deve ser maior que zero)
- `preco` → Real (obrigatório e deve ser maior que zero)

### 🔧 Operações Disponíveis

✅ Criar um novo produto no estoque.  
✅ Listar todos os produtos disponíveis.  
✅ Atualizar a quantidade e o preço de um produto existente.  
✅ Deletar um produto pelo ID.

## 🛠 Tecnologias Utilizadas

- **Python** 🐍
- **SQLite** 🗄️

 ## 📦 Módulos do Projeto

- `main.py`: ponto de entrada do programa, onde o código é executado.
- `menu.py`: exibe o menu principal e direciona as ações do usuário.
- `create.py`: cria o banco de dados e a tabela, se ainda não existirem.
- `insert.py`: insere novos produtos com seus respectivos atributos.
- `listar.py`: lista todos os produtos cadastrados com seus detalhes.
- `atualizar.py`: atualiza o preço ou a quantidade de um produto.
- `deletar.py`: remove um produto do banco de dados.
- `FunçõesVerificaçõesTipos.py`: contém funções auxiliares que validam se os valores inseridos são do tipo `float` ou `int`.


## 📌 Testes

### 🔹 Menu (Opções disponíveis: 1,2,3,4 ou 5)

```sh
# certo
Digite sua opção: 3
    🟢

# erro (opção fora das opções)
Digite sua opção: 7
    🔴 Mensagem retornada: "Digite uma opção válida!" e retorna o menu novamente

# erro (tipo errado)
Digite sua opção: idjfe
    🔴 Mensagem retornada: "Digite um tipo válido!" e retorna o menu novamente

```

### 🔹Criar produto

```sh
# 1 - certo
Informe o nome do produto: Abacaxi 
Informe a quantidade do produto: 100 
Informe o preço do produto: 6.7
    🟢 Produto inserido ao estoque com sucesso!! ID: {id}

# 2 - erro (tipo errado)
Informe o nome do produto: Banana  
Informe a quantidade do produto: lalala (string)  
Informe o preço do produto: lalala (string)
     🔴 Mensagem retornada até o usuário digitar o tipo correto: “Digite um tipo válido! “  

# 3 - erro (produto já existente)
Informe o nome do produto: Banana  
Informe a quantidade do produto: 50 
Informe o preço do produto: 3.5 
     🔴 Mensagem de retornada até o usuário digitar o tipo correto: "Digite uma opção válida!  "

# 4 - erro (preço negativo)
Informe o nome do produto: Maça  
Informe a quantidade do produto: 50 
Informe o preço do produto: -3.5 

# 5 - erro (nome vazio)
Informe o nome do produto:   
Informe a quantidade do produto: 50 
Informe o preço do produto: 3.4 

```

### 🔹Atualizar produto

```sh
# 6 - certo
Informe o [id] do produto que quer atualizar: 1 
Informe a nova quantidade do produto que quer atualizar: 50 
Informe o novo preço do produto que quer atualizar: 3.5 

# 7 - erro (tipo errado)
Informe o [id] do produto que quer atualizar: wwef 
Informe a nova quantidade do produto que quer atualizar: kscl 
Informe o novo preço do produto que quer atualizar: iojsxaij 

# 8 - erro (id inexistente)
Informe o [id] do produto que quer atualizar: 5 
Informe a nova quantidade do produto que quer atualizar: 50 
Informe o novo preço do produto que quer atualizar: 2.3 

# 9 - erro (quantidade negativa)
Informe o [id] do produto que quer atualizar: 1 
Informe a nova quantidade do produto que quer atualizar: -50 
Informe o novo preço do produto que quer atualizar: 2.3 

```


### 🔹Deletar produto

```sh
# 10 - certo
Informe o id do produto que deseja deletar: 1 

# 11 - erro (id não existe)
Informe o id do produto que deseja deletar: 5 
```



 
