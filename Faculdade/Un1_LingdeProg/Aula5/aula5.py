# Solicita ao usuário o valor do produto e o percentual de desconto
valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o valor do desconto (em %): "))

if percentual_desconto < 0 or percentual_desconto > 100: # Verifica se o desconto é válido
    print("Desconto inválido")
else:
    desconto = (percentual_desconto / 100) * valor_produto # Calculo do desconto
    valor_final = valor_produto - desconto # Calculo do valor final da compra
    print(f"Valor final do produto: R$ {valor_final:.2f}") # Exibe o valor final do produto com 2 casas decimais

