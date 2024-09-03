"""
    1. Dado um conjunto de alunos que frequentam um curso de Python e outro conjunto de
    alunos que frequentam um curso de Java, encontre:
    o Os alunos que frequentam apenas o curso de Python.
    o Os alunos que frequentam apenas o curso de Java.
    o Os alunos que frequentam ambos os cursos.
    o Os alunos que frequentam pelo menos um dos cursos
"""

python = {'Alice', 'Eduardo', 'Nicolas', "Lucas"}
java = {'Lucas'}

print(f"""
- Frequenta apenas o de Python: {python - java}
- Frequentam apenas o de Java: {java - python}
- Frequentam ambos: {python & java}
- Frequentm pelo menos um dos cursos: {python ^ java}
""")