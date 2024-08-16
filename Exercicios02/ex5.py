"""
    Defina uma função chamada concatenar_strings que aceite duas strings e um
    parâmetro nomeado separador com um valor padrão de espaço. A função deve
    retornar as duas strings concatenadas com o separador entre elas
"""

def concatenar_strings(a: str = "", b:str = "") -> str:
    """Concatena duas strings"""
    concatenar = a + " " + b
    return concatenar

a = input("Digite o começo de uma frase: ")
b = input("Digite o fim de uma frase: ")

print(f"Essa é a frase juntada/concatenada: \n{concatenar_strings(a,b)}")