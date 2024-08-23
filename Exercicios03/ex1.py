"""
    Escreva uma função que receba uma string e retorne o número de caracteres nela.
"""

def caracteres(frase: str = '') -> int:
    """Conta o número de caracteres de uma frase digitada pelo usuário"""
    frase = frase.replace(" ", "")
    return len(frase)

frase = input("Digite uma frase: ")
print(f"A frase contém {caracteres(frase)} caracteres!")
