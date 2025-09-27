# Conjunto ou set -> estrutura de dados que representa uma coleção de itens únicos e não ordenados
# Útil para eliminar duplicatas e realizar operações matemáticas como união, interseção e
# ---------
# Dicionário ou dict -> estruturas que associam chaves a valores.
# Permitem o armazenamento e a recuperação eficiente de informações.
# Útil para representar dados estruturados e permitir acesso rápido aos valores com base nas chaves
# ---------
# NumPy -> biblioteca para computação científica em Python.
# Fornece recursos avançados para manipulação de arrays multidimensionais, operações matemáticas e estatísticas.
# Muito utilizada em análise de dados, aprendizado de máquina e processamento de imagens
# ---------
# add() -> adiciona um elemento ao conjunto
# remove() -> remove um elemento do conjunto (gera erro se o elemento não existir)
# ---------

# Criando um conjunto vazio
meu_conjunto = set()

# Adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

# Imprimindo o conjunto
print("Conjunto após adições:", meu_conjunto)

# Verificando se um elemento está no conjunto
elemento = 20
if elemento in meu_conjunto:
    print(f"O elemento {elemento} está no conjunto.")
else:
    print(f"O elemento {elemento} não está no conjunto.")

# Removendo um elemento do conjunto
meu_conjunto.remove(20)
print("Conjunto após remoção:", meu_conjunto)

# --------------------------------------------------------------------------

# Objetos do tipo mapping -> Estruturas de dados que estabelecem uma relação entre chaves e valores
# Dicionários são exemplos de objetos do tipo mapping
# São mutáveis (podem ser alterados)

# Criando um dicionário vazio, seguido de atribuição de chaves e valores
dic1 = {}
dic1["nome"] = "Maria"
dic1["idade"] = 25

# Criando um dicionário com pares chave: valor
dic2 = {"nome": "Maria", "idade": 25}

# Criando um dicionário com uma lista de tuplas representando pares chave: valor
dic3 = dict([("nome", "Maria"), ("idade", 25)])

# Criando um dicionário com a função built-in zip() e duas listas, uma para chaves e outra para valores
dic4 = dict(zip(["nome", "idade"], ["Maria", 25]))

# Teste se todas as construções resultam em objetos iguais
print(dic1 == dic2 == dic3 == dic4)  # Deve imprimir True
print("Dicionário:", dic1)

# --------------------------------------------------------------------------

# Objetos do tipo array -> Estruturas de dados que armazenam coleções de itens do mesmo tipo
# Arrays são mais eficientes em termos de memória e desempenho para grandes volumes de dados numéricos
# NumPy é a biblioteca mais popular para trabalhar com arrays em Python
# NumPy fornece suporte para arrays multidimensionais e uma ampla gama de operações matemáticas
# NumPy oferece ferramentas para integração com C/C++ e Fortran, facilitando a interoperabilidade com código de alto desempenho
# Para usar NumPy, é necessário instalá-lo primeiro (pip install numpy)
# Para importar a biblioteca, usamos: import numpy as np
# NumPy lida com de maneira eficiente com matrizes de dados complexas e realizar operações matemáticas avançadas

# Importando a biblioteca NumPy
import numpy as np

# Criando um array NumPy a partir de números inteiros
my_array = np.array([1, 2, 3, 4, 5])

# Imprimindo o array
print("Array original:")
print(my_array)