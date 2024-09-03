"""
    Crie um dicionário chamado pessoas que contenha informações sobre pessoas.
        - Chave: cpf da pessoa
        - Valor: dicionário contendo nome, idade e cidade.
    Adicione pelo menos 5 pessoas ao dicionário.
    Crie uma função chamada 'pessoas_cidade' que exibe o nome de todas as pessoas que moram em uma
    cidade específica.
    Exemplo da estrutura a ser criada:
    pessoas = {
    '123.888.999-89': {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'},
    '845.678.658-02': {'nome': 'Bob', 'idade': 30, 'cidade': 'Rio de Janeiro'},
    '555.781.657-12': {'nome': 'Eva', 'idade': 22, 'cidade': 'São Paulo'}
    } 
"""

# Dicionário para armazenar as informações das pessoas
info_pessoas = {}

def preencher_info():
    """Preenche informações sobre as pessoas no dicionário"""
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")
    
    if idade.isdigit():
        info_pessoas[cpf] = {'nome': nome, 'idade': int(idade), 'cidade': cidade}
    else:
        print("Idade deve ser um número. Tente novamente.")
        preencher_info()

def pessoas_cidade(cidade):
    """Exibe o nome de todas as pessoas que moram em uma cidade específica."""
    nomes = []

    for pessoa in info_pessoas.values():
        if pessoa['cidade'] == cidade:
            nomes.append(pessoa['nome'])
    if nomes:
        print(f"Pessoas que moram em {cidade}: {', '.join(nomes)}")
    else:
        print(f"Nenhuma pessoa encontrada na cidade {cidade}.")

for _ in range(5):
    preencher_info()

cidade= input("Digite a cidade para buscar pessoas: ")
pessoas_cidade(cidade)
