"""
    Escreva um programa que receba uma frase como entrada e retorne uma lista das palavras
    presentes na frase.
"""
import os

def palavrasListas(frase: str = '')-> list:
    """Cria uma lista com as palavras que tem na frase"""
    return frase.split(' ')

def listarPalavras(lista:list = [])-> None:
    """Lista as Palavras de uma Frase"""
    os.system('cls')
    print("Lista das palavras da Frase: ")
    for i in lista:
        print(f"- {i.capitalize()}")

frase = input("Digite uma frase: ")

lista_palavras = palavrasListas(frase)
listarPalavras(lista_palavras)
