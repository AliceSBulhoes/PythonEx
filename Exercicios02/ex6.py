"""
    Crie uma função chamada comprar_produto que aceite dois parâmetros nomeados:
    produto e quantidade. O parâmetro produto deve ter um valor padrão de "produto
    desconhecido" e o parâmetro quantidade deve ter um valor padrão de 1. A função
    deve retornar uma mensagem indicando a compra do produto na quantidade
    especificada.
"""

def comprar_produto(produto: str = "Produto Desconhecido", quantidade: int = 1) -> str:
    """Realiza a compra de um produto"""
    retorno = f"Produto: {produto} \nQuantidade: {quantidade} \nProduto Comprado!"
    return retorno

def comeco():
    """Começa o programa"""
    opcao = input("Deseja comprar um produto/ [S/N]").upper()
    if opcao == "S":
        produto = input("Informe o produto: ")
        quantidade = int(input("Informe a quantidade: "))
        frase = comprar_produto(produto, quantidade)
        print(frase)
        comeco()
    elif opcao == "N":
        print("Obrigado! O Dickinson Group agradece!")
    else:
        print("Escreva S ou N")
        comeco()

comeco()