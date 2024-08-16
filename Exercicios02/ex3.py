"""
    Defina uma função chamada soma que aceite dois parâmetros numéricos (a e b) e
    retorne a soma desses números. Utilize anotações de tipos para indicar que os
    parâmetros e o retorno são do tipo float
"""

def soma(a: float, b: float) -> float:
    """Calcula a soma de dois valores"""
    soma = a + b
    return soma

a = float(input("Digite um número: "))
b = float(input("Digite um número: "))

soma = soma(a,b)

print(f"A soma dos dois valores é {soma}")