# 12 de Setembro de 2025 | Escola da Nuvem

temperatura = float(input("Digite a temperatura: "))
escala = input("Digite a escala (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
conversao = input("Digite a escala para a qual deseja converter (C, F, K): ").upper()

if escala == 'C'and conversao == 'F':
    resultado = (temperatura * 9/5) + 32
    print(f"{temperatura}°C é igual a {resultado}°F")
elif escala == 'C' and conversao == 'K':
    resultado = temperatura + 273.15
    print(f"{temperatura}°C é igual a {resultado}K")
elif escala == 'F' and conversao == 'C':
    resultado = (temperatura - 32) * 5/9
    print(f"{temperatura}°F é igual a {resultado}°C")
elif escala == 'F' and conversao == 'K':
    resultado = (temperatura - 32) * 5/9 + 273.15
    print(f"{temperatura}°F é igual a {resultado}K")
elif escala == 'K' and conversao == 'C':
    resultado = temperatura - 273.15
    print(f"{temperatura}K é igual a {resultado}°C")
elif escala == 'K' and conversao == 'F':
    resultado = (temperatura - 273.15) * 9/5 + 32
    print(f"{temperatura}K é igual a {resultado}°F")
else:
    print("INVÁLIDO")