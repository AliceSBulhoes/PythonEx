"""
    Escreva uma função que remova todos os espaços em branco de uma string e retorne a string
    resultante
"""

def juntar_tudo(frase: str = '')-> str:
    """Separa a string e junta ela tirando os espaços"""
    lista_palavra = frase.split(" ")
    frase_final = ''
    for i in lista_palavra:
        frase_final += i

    return frase_final

frase = input("Digite uma frase: ")
print(f"A frase, sem espaços, fica assim: {juntar_tudo(frase)}")
