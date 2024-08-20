"""
    Crie uma função que aceite um parâmetro nomeado itens que seja uma lista de
    strings. A função deve imprimir cada item da lista em linhas separadas.
"""

import os

def listar_itens(itens: list = [], nome: str = "Não Informado") -> None:
    """Lista os itens da lista"""
    n = 1
    os.system('cls')
    print(nome)
    for i in itens:
        print(f"{n}. {i}")
        n += 1
    print(" ")


def lista(num: str = 1) -> list:
    """Cria uma lista com os itens que usuário colocar"""
    lista = []
    
    for i in range(0,num):
        item_lista = input(f"Digite o item n°{i+1}: ")
        lista.append(item_lista)

    return lista


def verificar(num: str = 1) -> list:
    """Verifica se o num é um número inteiro"""
    if num.isdigit():
        return lista(int(num))
    else:
        print("Opção Inválida! Digite um número inteiro!")
        num = input("Digite o número de itens que seja ter em sua lista: ")
        verificar(num)

def comeco() -> None:
    """Começa o programa"""
    opcao = input("Deseja fazer uma lista? [S/N]: ").upper()
    if opcao == "S":
        nome = input("Digite o nome da lista desejada: ")
        num = input("Digite o número de itens que seja ter em sua lista: ")
        itens = verificar(num)
        listar_itens(itens, nome)
        comeco()
    elif opcao == "N":
        print("Obrigada por utilizar o software de Jacobi - Howe")
    else:
        print("Opção Inválida! Digite S ou N!")
        comeco()


comeco()