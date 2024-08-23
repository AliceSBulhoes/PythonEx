"""
    Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista
    com os números pares e outra com os números ímpares.
    Exemplo:
    Suponha que os números digitados são: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8].
    Para esta lista, o programa deve gerar as seguintes listas:
    [4, 8, 8]
    [1, 7, 9, 5, 3, 7, 9]
"""

import os

def criar_lista() -> None:
    """Cria uma lista com números inteiros digitados pelo usuário"""
    lista = []
    cont = 0
    while cont < 10:
        num = input("Digite um número: ")
        if not(num.isalpha()) :
            num = float(num)
            lista.append(num)
            cont += 1
        else:
            cont -= 1
            print("É para digitar um número !!!")

    mostrar(lista)

def pares_lista(lista: list = []) -> list:
    """Cria uma lista com os números impares da lista"""
    lista_par = []
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
    return lista_par

def impares_lista(lista: list = []) -> list:
    """Cria uma lista com os números impares da lista"""
    lista_imp = []
    for i in lista:
        if i % 2 != 0:
            lista_imp.append(i)

    return lista_imp

def mostrar(lista: list = []) -> None:
    """Mostra a média, o max e o min da lista"""
    lista_imp = impares_lista(lista)
    lista_par = pares_lista(lista)

    os.system('cls')

    print(f"Lista Pares")

    for i in range(0,len(lista_par)):
        print(f"- {lista_par[i]}\t")

    print(f"Lista Impares")

    for i in range(0,len(lista_imp)):
        print(f"- {lista_imp[i]}\t")

criar_lista()