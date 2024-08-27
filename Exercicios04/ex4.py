"""
    Conte a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é
    a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto.
    Exemplo:
    Para o texto abaixo:
        'faculdade de tecnologia fiap'
        A função deve retornar o seguinte dicionário:
        {'a': 4, 'u': 1, 'e': 3, 'o': 2, 'i': 2}
"""

vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

def contarVogais() -> None:
    """Conta as vogais de uma frase e armazena em um dict"""
    frase = input("Digite uma frase: ")
    for i in frase:
        for j in vogais.keys():
            if i == j:
                vogais[j] += 1

contarVogais()

print(vogais)
