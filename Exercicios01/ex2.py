"""
    Implemente a função quadrado que recebe um número e retorna o resultado desse número ao
    quadrado.
"""

def quadrado(x: float) -> float:
    """Faz o ao quadrado de um número digitado pelo usuário"""
    quadrado = x**2
    return quadrado

x = float(input("Digite um número: "))
quadrado = quadrado(x)

print(f"O ao quadrado de {x} é {quadrado:.2f}")
