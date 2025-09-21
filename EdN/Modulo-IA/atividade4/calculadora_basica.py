# 16 de Setembro de 2025 | Escola da Nuvem

# Dados de Entrada
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

# Escolha da operação
operação = input("Escolha a operação (+, -, *, /): ")

# Cálculo
if operação == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é {resultado}")
elif operação == "-":
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é {resultado}")
elif operação == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é {resultado}")
elif operação == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")