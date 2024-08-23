"""
    Crie uma função que retorne a quantidade de vogais (a, e, i, o, u) existentes em uma string.
"""
vogais = ['a', 'e', 'i', 'o', 'u']

def contarVogais(frase: str = '')-> int:
    """Conta as vogais de uma frase"""
    contar = 0
    for i in vogais:
        contar += frase.lower().count(i)

    return contar

frase = input("Digite uma frase: ")
print(f'A frase contém {contarVogais(frase)} vogais')
