"""
    Dada uma lista com vários elementos (alguns podem ser duplicados), crie um set a
    partir dessa lista e conte a quantidade de elementos únicos.
"""

lista = ["maçã", "maçã", "tangerina", "limão", "limão", 18, 1, 1, 72, 18, 51, 49]

sets = set(lista)

print(f"Elementos únicos na lista: {len(sets)}")