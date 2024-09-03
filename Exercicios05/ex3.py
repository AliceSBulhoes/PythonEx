"""
    Crie um dicionário chamado 'estoque' com informações sobre alguns produtos:
        - Chave: Nome do produto
        - Valor: Tupla contendo preço e quantidade em estoque
    Adicione pelo menos 5 produtos ao dicionário.
    Crie uma função chamada 'total_valor_estoque' que calcula o valor total do estoque (preço * quantidade) para
    todos os produtos no dicionário.
    Exemplo da estrutura a ser criada:
    estoque = {'caneta': (4.70, 40), 'caderno': (45.0, 20), 'lápis': (3.50, 10)}
"""
import os

estoque = {}

def preencherInfo() -> None:
    """Preenche uma tupla e depois um dict com as infos dos produtos"""
    produto = input("Nome do Produto: ")
    preco = float(input("Preço: "))
    qtd = int(input("Quantidade no estoque: "))

    tupla_produto = (preco, qtd)
    estoque[produto] = tupla_produto

def totalValorEstoque() -> float:
    """Calcula o valor total do estoque"""
    valorTotal = 0

    for key, valor in estoque.items():
        preco, quantidade = valor
        valorEstoque = preco * quantidade
        valorTotal += valorEstoque
        print(f"Produto: {key}\nValor no Estoque: {valorEstoque:.2f}")

    print(f"Total do Valor do Estoque: {valorTotal:.2f}")
    return valorTotal

# Preenchendo o estoque com pelo menos 5 produtos
for i in range(5):
    preencherInfo()

print(f"\nEstoque Atual: {estoque}")

totalValorEstoque()
