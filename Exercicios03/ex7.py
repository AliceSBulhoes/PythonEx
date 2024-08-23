"""
    Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
        a) o maior número da lista
        b) o menor número da lista
        c) a média dos números contidos na lista
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

def max_lista(lista: list = []) -> int:
    """Define o máximo da lista"""
    return max(lista)

def min_lista(lista:list = []) -> int:
    """Define o minimo da lista"""
    return min(lista)

def media_lista(lista:list = []) -> float:
    """Define a média dos números da lista"""
    media = sum(lista) / 10
    return media

def mostrar(lista: list = []) -> None:
    """Mostra a média, o max e o min da lista"""
    os.system('cls')
    print(f"""
A média da lista é: {media_lista(lista)};
A maximo da lista é: {max_lista(lista)};
A mínimo da lista é: {min_lista(lista)};
""")
    
criar_lista()
