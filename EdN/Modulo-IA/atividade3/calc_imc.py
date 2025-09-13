# 12 de Setembro de 2025 | Escola da Nuvem

# Cálculo de IMC

# Dados de entrada
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo
imc = peso / (altura ** 2)

# Resultado
print(f"Seu IMC é: {imc:.2f}")

# Classificação
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso normal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >=30:
    print("Você está com obesidade.")