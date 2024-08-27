"""
    Preencha duas tuplas com 5 números cada, informados pelo usuário. Concatene as duas
    tuplas e exiba a tupla resultante.
    Exemplo: Suponha que as tuplas contenham os números:
        (3, 1, 5, 3, 5)
        (5, 5, 7, 3, 1).
    Como resultado, o programa deve gerar a tupla:
        (3, 1, 5, 3, 5, 5, 5, 7, 3, 1).
"""
import os

def criacaoTupla() -> tuple:
    """Cria uma tupla com valores inseridos pelo usuário"""
    lista = []
    cont = 0

    os.system('cls')

    while cont < 5:
        num = input("Digite um número: ")
        if not(num.isalpha()) :
            num = float(num)
            lista.append(num)
            cont += 1
        else:
            cont -= 1
            print("É para digitar um número !!!")
    
    return tuple(lista)

def concatenacao(tupla1: tuple = (), tupla2: tuple = ()) -> tuple:
    """Concatena duas tuplas diferentes"""
    tupla_final = tupla1 + tupla2

    return tupla_final
 
tupla1 = criacaoTupla()
tupla2 = criacaoTupla()

print(f"A tupla final ficou: {concatenacao(tupla1, tupla2)}")
