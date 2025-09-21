# s -> string (sequência de caracteres) ou o objeto
# x in s -> True caso um item de s seja igual a x, False caso contrário
# s + t -> concatena s com t (une as duas strings)
# s * n -> repete s n vezes
# s[i] -> acessa o valor guardado na posição i de s
# s[i:j] -> acessa os valores da posição i até a j
# s [i:j:k] -> acessa os valores da posição i até a j, pulando k posições
# len(s) -> retorna o tamanho de s
# min(s) -> retorna o menor valor de s
# max(s) -> retorna o maior valor de s
# s.count(x) -> retorna o número de vezes que x aparece em s
# s.index(x) -> retorna a posição da primeira vez que x aparece em s

texto = "explorando a diversidade de linguagens de programação com Python"
print(f"Tamanho do texto: {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print("Quantidade de 'e':", texto.count('e'))
print("As 5 primeiras letras:", texto[:5])

# As listas são estrututras de dados mutáveis (podem ser alteradas)
# Listas são indexadas (cada elemento tem uma posição)
cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
for cor in cores:
    print(f"Posição = {cores.index(cor)}, cor = {cor}")

# listcomps (list comprehensions) -> cria listas com base em objetos iteráveis
# Bom para quando queremos transformar ou filtrar as informações de uma sequência existente para construir uma nova
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
print("Antes da listcomp:", linguagens)

linguagens = [item.lower() for item in linguagens] # Transforma todos os itens em letras minúsculas
print("Depois da listcomp:", linguagens)

# map() -> aplica uma função a todos os itens de um objeto iterável
precos_em_dolar = [100, 50, 75, 120]
taxa_de_cambio = 5.25
precos_em_real = list(map(lambda x: x * taxa_de_cambio, precos_em_dolar))
print("Preços em real:", precos_em_real)

# filter() -> filtra os itens de um objeto iterável com base em uma função que retorna True ou False
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", numeros_pares)

# TUPLAS -> são estruturas de dados imutáveis (não podem ser alteradas)
# São indexadas (cada elemento tem uma posição)
# Usadas para armazenar coleções de dados que não devem ser alteradas
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo de objeto vogais: {type(vogais)}")
for p, x in enumerate(vogais):
    print(f"Posição = {p}, vogal = {x}")

