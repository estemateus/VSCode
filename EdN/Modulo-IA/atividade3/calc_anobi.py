# 13 de Setembro de 2025 | Escola da Nuvem

# Cálculo de ano bissexto
ano = int(input("Digite um ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")