# 12 de Setembro de 2025 | Escola da Nuvem

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso normal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >=30:
    print("Você está com obesidade.")