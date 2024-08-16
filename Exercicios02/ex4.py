"""
    Crie uma função chamada enviar_email que aceite os parâmetros destinatario,
    assunto e corpo. O parâmetro assunto deve ter um valor padrão de "Sem assunto".
    O parâmetro corpo deve ter um valor padrão de uma string vazia. A função deve
    imprimir as informações formatadas. Inclua uma docstring que explique brevemente
    o propósito da função
"""

def enviar_email(destinario: str = "Não Informado", assunto: str = "Sem assunto", corpo: str = ""):
    """Envia um email para um destinatario especifico"""
    print("------------------------------")
    print(f"Destinatario: {destinario}")
    print(assunto)
    print(corpo)
    print("------------------------------")

destinatario = input("Digite o destinatário: ")
assunto = input("Digite o assunto do email: ")
corpo = input("Digite o conteudo do email: \n")

enviar_email(destinatario, assunto, corpo)