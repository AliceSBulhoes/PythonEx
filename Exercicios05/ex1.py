"""
    Escreva um programa que recebe uma frase como entrada e retorna um dicionário onde as chaves são as
    palavras únicas na frase e os valores são o número de vezes que cada palavra aparece.
    Exemplo:
    Para o texto abaixo:
    'Exemplo de texto para contagem de palavras no texto'
    Deve ser gerado o dicionário:
    {'Exemplo': 1, 'de': 2, 'texto': 2, 'para': 1, 'contagem': 1, 'palavras': 1, 'no': 1}
"""

palavras = {}

def cortarFrase(frase: str = '') -> list:
    """Corta a frase nos espaços vazios"""
    frase_cortada = frase.split(' ')
    return frase_cortada


def adicionarDic(lista: list = []) -> None:
    """Adiciona as palavras no dicionário"""
    for i in lista:
        if not(i in palavras):
            palavras[i] = 1
        else:
            palavras[i] += 1

frase = input("Digite uma frase: ")

frase_cortada = cortarFrase(frase)
adicionarDic(frase_cortada)
print(f'Dicionário de palavras: {palavras}')






