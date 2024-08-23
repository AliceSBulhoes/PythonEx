"""
    Preencha duas listas, uma para armazenar os nomes e outra para armazenar as idades de
    pessoas. A entrada de dados deve ser finalizada quando o usuário informar um nome vazio.
    Na sequência informe o nome de todas as pessoas que possuem idade igual ou superior a
    18 anos
"""

import os

def criar_lista() -> list:
    """Cria duas listas: uma com nome e outra com a idade da pessoa"""
    cont = 1
    nome = []
    idade = []

    lista = []

    while True:
        nome_user = input("Nome: ")
        idade_user = input("Idade: ")

        if idade_user.isalpha():
            print("Idade inválida! Insira novamente o nome e a idade!")
            continue
        elif nome_user == '' or idade_user == '':
            break
        else:
            nome.append(nome_user)
            idade.append(int(idade_user))

    lista.append(nome)
    lista.append(idade)

    return lista

def maiores_idade(lista:list = [] ):
    """Lista a o nome e a idade dos maiores de idade"""
    os.system('cls')
    for i in range(0,len(lista[1])):
        if lista[1][i] >= 18:
            print(f"Nome: {lista[0][i]}\tIdade: {lista[1][i]}")        


lista = criar_lista()
maiores_idade(lista)