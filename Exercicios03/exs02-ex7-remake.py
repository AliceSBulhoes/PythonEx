"""
    Crie uma função que aceite um parâmetro nomeado itens que seja uma lista de
    strings. A função deve imprimir cada item da lista em linhas separadas.
"""

import os

dic_listas = {}

def listar_itens(itens: list = [], nome: str = "Não Informado") -> None:
    """Lista os itens da lista"""
    n = 1
    print(nome)
    for i in itens:
        print(f"{n}. {i}")
        n += 1
    print(" ")

    dic_listas[nome] = itens


def lista(num: int = 1) -> list:
    """Cria uma lista com os itens que usuário colocar"""
    lista = []
    for i in range(0,num):
        item_lista = input(f"Digite o item n°{i+1}: ")
        lista.append(item_lista)
    return lista


def listar_todos() -> None:
    for nome,itens in dic_listas.items():
        print("-" * 35)
        listar_itens(itens,nome)


def comeco() -> None:
    """Começa o programa"""
    opcao = input("Deseja fazer uma lista? [S/N]: ").upper()
    if opcao == "S":
        num = int(input("Digite o número de itens que seja ter em sua lista: "))
        nome = input("Digite o nome da lista desejada: ")
        itens = lista(num)
        os.system('cls')
        listar_itens(itens, nome)
        comeco()
    elif opcao == "N":
        opcao2 = input("Deseja ver todas as listas ? [S/N]: ").upper()
        if opcao2 == "S":
            os.system('cls')
            listar_todos()
            print("-" * 35)
        elif opcao2 == "N":
            print("Obrigado por Utilizar o Software!")
        else:
            ...
    else:
        print("Opção Inválida! Digite S ou N!")
        comeco()

os.system('cls')
comeco()
