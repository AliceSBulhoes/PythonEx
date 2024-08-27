"""
    Preencha um dicionário com os dados de 5 alunos.
        - Utilize o RM do aluno como chave e uma lista de três notas como valor.
        - Solicite os dados ao usuário.
    Percorra o dicionário e exiba a média de cada aluno.
    Exemplo:
        Veja um exemplo da estrutura do dicionário.
        {1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}
"""

import os

alunos = {}

def preencherInfo() -> None:
    """Preenche os alunos de uma loja dadas pelo usuário e o coloca no dic"""
    key = input("Digite o RM: ")
    notas = []

    for i in range(0,3):
        nota = float(input(f"Digite a nota da prova {i+1}: "))
        notas.append(nota)

    alunos[key] = notas


def mostrar50(dic: dict = {}) -> None:
    """Mostra na tela os preços dos alunos superios a 50"""
    os.system('cls')
    for key, notas in dic.items():
        print(f"\nRM: {key}\nMédia: R${sum(notas)/3}")


for i in range(0,5):
    preencherInfo()

mostrar50(alunos)