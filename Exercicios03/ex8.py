"""
    Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
        a) a quantidade de números pares contidos na lista
        b) o somatório de todos os números ímpares contidos na lista
"""

import os

def criar_lista() -> None:
    """Cria uma lista com números inteiros digitados pelo usuário"""
    lista = []
    cont = 0
    while cont < 10:
        num = input("Digite um número inteiro: ")
        if num.isdecimal():
            num = int(num)
            lista.append(num)
            cont += 1
        else:
            cont -= 1
            print("É para digitar um número inteiro!!!")

    mostrar(lista)

def pares_contar(lista: list = []) -> int:
    """Conta os números pares da lista"""
    cont = 0
    for i in lista:
        if i % 2 == 0:
            cont += 1
    return cont

def impares_contar(lista: list = []) -> int:
    """Conta os números impares da lista"""
    cont = 0
    for i in lista:
        if i % 2 != 0:
            cont += i

    return cont

def mostrar(lista: list = []) -> None:
    """Mostra a média, o max e o min da lista"""
    os.system('cls')
    print(f"""
A quantidade de pares na lista é : {pares_contar(lista)};
O somatório de todos os números ímpares contidos na lista: {impares_contar(lista)};
""")
    
criar_lista()
