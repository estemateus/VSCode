# Lista de notas do estudante
notas = [7.5, 8.0, 6.5, 9.0, 7.0]

# Função regular para calcular a média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

# Calcular a média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificar se o estudante foi aprovado
if media_arredondada >= 7.0:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Exibir os resultados
print(f"As notas do estudante são: {notas}")
print(f"A média das notas é: {media_arredondada}")
print(f"A situação do estudante é: {situacao}")