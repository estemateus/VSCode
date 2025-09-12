# 08 de Setembro de 2025 | Escola da Nuvem

# Conversor de Moeda

# Solicita ao usuário o valor em Reais
valor_reais = float(input("Digite o valor em Reais (R$): "))
cotacao_dolar = 5.42
cotacacao_euro = 6.36

# Cálculo da conversão
conversao_dolar = valor_reais / cotacao_dolar
conversao_euro = valor_reais / cotacacao_euro

# Exibindo os resultados
print(f"O valor em Reais (R$) é: {valor_reais:.2f}")
print(f"O valor em Dólares (US$) é: {conversao_dolar:.2f}")
print(f"O valor em Euros (€) é: {conversao_euro:.2f}")