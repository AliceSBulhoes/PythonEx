"""
    Crie uma função chamada calcular_area_retangulo que aceite dois parâmetros:
    base e altura, ambos com valores padrão iguais a 1. A função deve retornar a área
    do retângulo.
"""

def calcular_area_retangulo(base: float = 1, altura:float = 1) -> float:
    """Calcula a area de um retangulo"""
    area = base*altura
    return area

base = float(input("Digite a base (m): "))
altura = float(input("Digite a altura (m): "))

area = calcular_area_retangulo(base,altura)

print(f"A área do retângulo é {area} m²")
