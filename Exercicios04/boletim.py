import random

alunos = {}


def cadastrarRM() -> str:
    """Cadastra um aluno com um RM aleatório"""
    rm_aluno = 'RM'
    for i in range(0,6):
        rm_aluno += str(random.randint(1,9))
    
    return rm_aluno

def cadastrarAluno(rm: str = '') -> None:
    """Cadastra os dados do Aluno"""
    nome = input("Nome do Aluno: ")
    idade = input("Idade do Aluno: ")
    sala = input("Sala do Aluno: ")

    if not(idade.isalpha) or not(idade.isdecimal):
        rm = cadastrarRM()
        alunos[rm]['nome'] = nome
        alunos[rm]['idade'] = idade
        alunos[rm]['sala'] = sala
    else:
        print("Idade inserida incorretamente! Tente Novamente!")
        cadastrarAluno()

def menu() -> None:
    opcao = input("""Deseja realizar qual das sequintes opções (Digite a opção):
    C - Cadastrar Aluno
    I - Inserir Nota
    B - Ver Boletim do Aluno""")
