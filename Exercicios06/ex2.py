"""
    Dada uma lista com alguns elementos duplicados, converta a lista em um set para
    remover duplicatas e depois converta de volta para uma lista.
"""

lista = ['Hello Word', "Hell Word", "Hello Word", "maça", "maça", 'sabotagem']

sets = set(lista)

lista_dnv = list(sets)

print(lista_dnv)