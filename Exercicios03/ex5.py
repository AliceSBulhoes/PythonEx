"""
    Implemente uma função que retorne a quantidade de palavras existentes em uma string.
"""

def contarPalavras(frase: str = '')-> int:
    """Conta as palavras de uma frase"""
    listaPalavras = frase.split(" ")
    return len(listaPalavras)

frase = input("Digite uma frase: ")
print(f'A frase contém {contarPalavras(frase)}')