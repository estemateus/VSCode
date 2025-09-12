# 09 de Setembro de 2025 | Escola da Nuvem

# Cálculo da Média Escolar

# Solicita ao usuário o nome do aluno e suas notas
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibindo o resultados
print(f"Aluno: {nome_aluno}")
print(f"Notas: {nota1:.2f}, {nota2:.2f}, {nota3:.2f}")
print(f"Média: {media:.2f}")