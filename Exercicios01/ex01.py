"""
    Implemente a função somar que recebe dois números e retorna o resultado da soma desses dois
    números.
    Lembre-se que para retornar um resultado a função deve utilizar a instrução return.
"""

def somar(x: float, y:float) -> float:
    """Calcula a soma de dois número digitado pelo usuário"""
    soma = x + y
    return soma

x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
soma = somar(x,y)

print(f"A soma é {soma: .2f}")
