"""
    Implemente a função soma_divisores, que recebe como parâmetro de entrada um número positivo
    e retorna a soma de todos os divisores desse número.
    Por exemplo:
        - Caso o número seja 15, o retorno deve ser 24 (1 + 3 + 5 + 15).
        - Caso o número seja 30, o retorno deve ser 72 (1 + 2 + 3 + 5 + 6 + 10 + 15 + 30)
"""

divisores = []

def soma_divisores(x: int) -> int:
    """Soma os divisores de um número fornecido pelo usuário"""
    for i in range(1, x + 1):
        if x % i == 0:
            divisores.append(i)
            if x != i:
                print(f"{i} + ", end="")
            else:
                print(f"{i} = {sum(divisores)}")

    return sum(divisores)

x = int(input("Digite um número inteiro: "))
somaDivisores = soma_divisores(x)

print(f"A soma dos divisores é {somaDivisores}")
