"""
    Crie dois sets, um com números pares e outro com números ímpares. Os números
    devem variar de 1 a 10.
    o União: Obtenha a união dos dois sets.
    o Interseção: Obtenha a interseção dos dois sets.
    o Diferença: Obtenha a diferença dos sets (elementos que estão no primeiro set
    e não no segundo).
"""

set_par = {2,4,6,8,10}
set_impar = {1,3,5,7,9}

print(f"""
- União: {set_par | set_impar};
- Intersecção: {set_par & set_impar};
- Diferença: {set_par - set_impar}
""")