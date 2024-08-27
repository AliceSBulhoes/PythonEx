"""
    Preencha um dicionário com as informações de 5 produtos.
        - Utilize o nome do produto como chave e o preço como valor.
        - Solicite os dados ao usuário.
    Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00
    Exemplo:
        Veja um exemplo da estrutura do dicionário.
        {'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0}
"""
import os

produtos = {}

def preencherInfo() -> None:
    """Preenche os produtos de uma loja dadas pelo usuário e o coloca no dic"""
    key = input("Digite o produto: ")
    value = float(input("Digite o valor do produto: "))

    produtos[key] = value


def mostrar50(dic: dict = {}) -> None:
    """Mostra na tela os preços dos produtos superios a 50"""
    os.system('cls')
    for key, preco in dic.items():
        if preco > 50:
            print(f"Produto: {key}\nPreço: R${preco}")


for i in range(0,5):
    preencherInfo()

mostrar50(produtos)
