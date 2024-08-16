"""
    Escreva uma função chamada mostrar_informacoes que aceite três parâmetros
    nomeados: nome, idade e cidade. A função deve imprimir uma mensagem
    formatada com essas informações.
"""

def mostrar_informacao(nome: str = "Não Informado", idade: int = 0, cidade: str = "Não Informado") -> None:
    """Imprimi uma mensagem com as informações fornecidas"""
    print(f"Nome   : {nome}")
    print(f"Idade  : {idade}")
    print(f"Cidade : {cidade}")


# Parâmetros Nomeados

mostrar_informacao("Tara", 40, "Gaylordstad")