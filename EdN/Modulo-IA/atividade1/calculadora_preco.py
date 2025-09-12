# 08 de Setembro de 2025 | Escola da Nuvem

# Calcule o preço total de um produto

# Informações do produto
nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))

# Calcula o preço total
preco_total = preco_unitario * quantidade

# Exiba o resultado na tela
print(f"\nProduto: {nome_produto}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço Total: R$ {preco_total:.2f}")