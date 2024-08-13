"""
    Implemente a função calcular_salario, que recebe o salário atual de um funcionário e retorna o
    salário com um reajuste de aumento, sendo que:
        - Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
        - Caso contrário, o funcionário receberá 15% de aumento.
"""

def calcular_salario(salarioAtual: float) -> float:
    """Calcula o ajuste do salário"""
    if salarioAtual > 2000:
        salarioAjustado = salarioAtual * 1.07
    else:
        salarioAjustado =salarioAtual * 1.15
    return salarioAjustado

salarioAtual = float(input("Digite o seu salário: "))
salarioAjustado = calcular_salario(salarioAtual)

print(f"Seu novo salário é de {salarioAjustado}")
