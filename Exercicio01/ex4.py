"""
    Implemente a função media, que recebe três valores numéricos e retorna a média aritmética dos
    valores
"""

def media(x: float, y:float, z:float) -> float:
    """Calcula a média de três valores"""
    media = (x + y + z) / 3
    return media

x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
z = float(input("Digite um número: "))
media = media(x,y,z)

print(f"A média dos valores é {media: .2f}")
