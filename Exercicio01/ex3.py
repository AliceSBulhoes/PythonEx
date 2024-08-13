"""
    Implemente a função soma_dos_quadrados que receba dois numeros e devolve a soma dos seus
    quadrados.
    Você pode tentar reutilizar a função quadrado definida anteriormente para facilitar a implementação
"""
def soma_dos_quadrados(x: float, y:float) ->float:
    """Calcula a soma dos quadrados de números fornecidos pelo usuário"""
    somaQuadrado = (x**2) + (y**2)
    return somaQuadrado

x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
somaQuadrados = soma_dos_quadrados(x,y)

print(f"A soma dos quadrados dos números {x} e {y} é {somaQuadrados}")
