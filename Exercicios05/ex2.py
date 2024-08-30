"""
    Crie uma lista de tuplas, onde cada tupla contém informações sobre um aluno:
    (Nome do aluno, Idade, Nota)
    Escreva uma função chamada 'alunos_aprovados' que recebe a lista de alunos e retorna uma nova lista apenas
    com os nomes dos alunos que têm uma nota maior ou igual a 7.
    Exemplo da estrutura a ser criada:
        alunos = [('Alice', 20, 8.5), ('Bob', 18, 5.0), ('Eva', 22, 7.5)]
    Exemplo de Retorno:
        ['Alice', 'Eva']
"""

import os

lista_alunos = []

def preencherInfo() -> tuple:
    """Preenche tuplas com informação"""
    nome = input("Nome: ")
    idade = input("Idade: ")
    nota = input("Nota: ")

    if not(idade.isalpha or idade.isdigit or nota.isalpha):
        os.system('cls')
        print("Idade ou Nota inserida incorretamente! Tente Novamente!")
        preencherInfo()
    else:
        tupla_info = (nome, int(idade), float(nota))
        return tupla_info

def adicionarLista(tupla:tuple = ()) -> list:
    """Adiciona a tupla em uma lista"""
    lista_alunos.append(tupla)
    return lista_alunos


def alunos_aprovados(lista:list = []) -> list:
    """Retorna uma lista dos alunos aprovados (nota maior ou igual a 7)"""
    lista_aprovados = []

    for i in lista:
       if i[2] >= 7.0:
           lista_aprovados.append(i[0])
    
    return lista_aprovados

preencherInfo()

while True:
    opcao = input("Deseja adiconar mais? [S/N]: ").upper()
    if opcao == 'N':
        break
    elif opcao == 'S':
        adicionarLista(preencherInfo())
    else:
        print("Opção inválida! Tente Novamente...")
        continue

print(f"Alunos aprovados são: {alunos_aprovados(lista_alunos)}")

    
