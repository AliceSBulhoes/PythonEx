"""
    Crie uma função que receba uma string e retorne a mesma string com todas as letras em
    maiúsculas.
"""

def maiusclo(frase: str = '')-> str:
    """Transforma as letras da frase para Maiusculo"""
    return frase.upper()

frase = input("Digite uma frase: ")
print(f"A frase em maiusculo fica: {maiusclo(frase)}")
