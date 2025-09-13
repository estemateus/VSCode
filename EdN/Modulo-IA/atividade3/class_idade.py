# 12 de Setembro de 2025 | Escola da Nuvem

# Classificação por idade
idade = int(input("Digite sua idade: "))
if idade > 0 and idade <= 12:
    print("Você é uma criança")
elif idade > 12 and idade <= 17:
    print("Você é um adolescente")
elif idade > 17 and idade <= 59:
    print("Você é um adulto")
elif idade >= 60:
    print("Você é um idoso")
else:
    print("Idade inválida")