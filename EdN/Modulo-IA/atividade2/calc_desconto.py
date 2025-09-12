# 09 de Stembro de 2025 | Escola da Nuvem

# Cálculo de Desconto

# Solicita ao usuário o valor do produto
produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto: "))
desconto = int(input("Digite a porcentagem de desconto: "))

# Cálculo do valor com desconto
valor_desconto = valor_produto * (desconto / 100)
valor_final = valor_produto - valor_desconto

# Exibindo os resultados
print(f"O produto é: {produto}")
print(f"O valor do produto é: R${valor_produto:.2f}")
print(f"O valor do desconto é: R${valor_desconto:.2f}")
print(f"O valor final do produto é: R${valor_final:.2f}")