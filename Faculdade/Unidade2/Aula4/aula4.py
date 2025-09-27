# BIBLIOTECAS E MÓDULOS EM PYTHON

# Existem duas abordagens principais para se organizar o código em Python:
# 1. Usando funções ou classes para encapsular funcionalidades.
# 2. Dividindo o código em vários arquivos .py para modularizar a solução.
# O ideal é combinar essas técnicas, criando módulos separados em arquivos independentes.

# MÓDULOS
# Um módulo é um arquivo .py que contém definições e implementações de funções, classes e variáveis.
# Módulos são componentes de código que servem como bibliotecas ou conjuntos de funções em Python.
# Abrigam uma variedade de funcionalidades, incluindo operações matemáticas, interações com o sistema operacional, manipulação de arquivos, entre outras.
# Na prática, um módulo pode ser considerado uma biblioteca de códigos.

# EXEMPLO DE MÓDULO
# Módulo 'math' -> fornece funções matemáticas.
# Módulo 'os' -> disponibiliza funções relacionadas ao sistema operacional, como como obtenção do diretório de trabalho atual (getcwd), listagem de arquivos em um diretório (listdir), criação de pastas (mkdir), entre muitos outros recursos.
# Esses módulos são bibliotecas de funções relacionadas a áreas específicas, viabilizando a reutilização de código.

# UTILIZAÇÃO DE MÓDULOS
# Para utilizar um módulo em Python, usamos a palavra-chave 'import' seguida do nome do módulo.

# Primeiro modo
import math

math.sqrt(25)  # Calcula a raiz quadrada
math.log2(1024)  # Calcula o logaritmo na base 2
math.cos(45)  # Calcula o cosseno

# Segundo modo
import math as m # Renomeia o módulo para 'm'
m.sqrt(25)
m.log2(1024)
m.cos(45)

# Terceiro modo
from math import sqrt, log2, cos # Importa funções específicas do módulo
sqrt(25)
log2(1024)
cos(45)

# CLASSIFICANDO MÓDULOS
# Módulos embutidos (built-in): Incluídos na instalação padrão do Python (ex: math, os, sys, svs, Random, datetime, re, collections).
# Módulos de terceiros: Criados por terceiros e disponibilizados via PyPI (Python Package Index). Instalados via gerenciadores de pacotes como pip (ex: numpy, pandas, requests, matplotlib).
# Módulos personalizados: Criados pelo usuário.

# MATPLOTLIB
# Umas biblioteca de vizualização
# Oferece uma ampla gama de recursos para criar gráficos e vizualizações de dados de maneira flexível e personalizável.
# É utilizado para construir gráficos estáticos, interativos e animações.

# Importa o módulo pyplot do Matplotlib como plt
import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Criar um gráfico de linha
plt.plot(x, y)

# Adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar um título ao gráfico
plt.title('Exemplo de Gráfico em Linha')

# Mostrar o gráfico
plt.show()