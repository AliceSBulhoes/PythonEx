# Parâmetro Default

def cadastrar_funcionario(nome:str = "Não Informado",idade:int = 0, salario:float = 0.0)-> None:
    """Exibe informações de um funcionário"""
    print(f"Nome    : {nome}")
    print(f"Idade   : {idade}")
    print(f"Salario : R$ {salario}")
    print("--------------------------")

# Parâmetro Posicional

cadastrar_funcionario("Robertinho", 40, 2300.50)

# Parâmetro Vazio

cadastrar_funcionario()

# Parâmetro Nomeado

cadastrar_funcionario(salario=2500)

# Parâmetro Posicional e Nomeado
"""Os parâmetros posicionais sempre devem ser utilizados antes dos nomeados"""

cadastrar_funcionario("Stanford", salario = 2400)
