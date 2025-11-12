# INTRODUÇÃO A BIBLIOTECA PANDAS

# SOBRE O PANDAS:
# Uma biblioteca Python de alto desempenho e código aberto
# Foi projetada para simplificar a manipulação e a análise de dados organizados em tabelas e séries temporais
# Disponibiliza estrturas de dados poderosas, como DataFrames e Series, que possibilitam uma abordagem mais intuitiva e eficiente ao lidar com dados tabulares
# É amplamente utilizado em análise de dados, ciência de dados e engenharia de dados por sua maneira amigável e eficiente de lidar com dados.

# Características notáveis do Pandas:
# 1. DataFrames: Estrtura bidimensional, semelhante a uma tabela. Altamente flexível e acomoda diversos tipos de dados.
# 2. Series: Estrutura unidimensional, semelhante a uma lista/matriz. Altamente flexível e acomoda diversos tipos de dados.
# 3. Manipulação de dados: o pandas oferece uma gama de funções e métodos para realizar tarefas comuns de manipulação de dados, como filtragem, seleção, ordenação, agrupamento e agregação.
# 4. Leitura e escrita de dados: suporta a leitura e escrita de dados em vários formatos, incluindo CSV, Excel, SQL, HDF5 e muitos outros, tornando-se uma ferramenta versátil para lidar com dados de diferentes fontes.
# 5. Tratamento de dados ausentes: Simplifica o tratamento de dados faltantes, permitindo que os desenvolvedores preencham ou removam valores ausentes de forma eficaz.
# 6. Visualização de dados: Pode ser integrado a outras bibliotecas de visualização, como Matpltlib e seaborn, para criar gráficos e visualizações informativas.
# 7. Integração com NumPy: É construído sobre a biblioteca NumPy, ou seja, pode-se combinar as capacidades NumPy para cálculos matemáticos às funcionalidades do pandas para manipulação de dados.
# 8. Comunidade ativa: O pandas tem uma comunidade de usuários e desenvolvedores ativa, o que resulta em suporte contínuo e atualizações regulares.

# SERIES
# Para criar um objeto do tipo Series no Pandas, utilizamos o método Series() ccom vários parâmetros opcionais.
# O principal parâmetro é 'data', que pode conter um único valor, uma lista de valores ou um dicionário.
# Outros parâmetros, como 'index', 'dtype' e 'name', têm valores-padrão predefinidos, tornando sua especificação opcional.

# EXEMPLO 1 - CRIAR UMA SERIES A PARTIR DE UMA LISTA
import pandas as pd

# Criando uma lista de valores
data = [10, 20, 30, 40, 50]

# Criando uma Series a partir da lista
series1 = pd.Series(data)

print(series1)

# EXEMPLO 2 - CRIANDO UMA SERIES A PARTIR DE UM DICIONÁRIO
import pandas as pd

# Criando um dicionário com pares chave-valor
data = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

# Criando uma Series a partir do dicionário
series2 = pd.Series(data)

print(series2)

# -- LEITURA DE DADOS ESTRUTURADOS COM A BIBLIOTECA PANDAS --

# O pandas consegue ler dados estruturados e armazená-los em um DataFrame
# Ele oferece vários métodos de leitura de dados, identificados pelo padrão 'read', como 'pandas.read_XXXXX()'
# Cada método é projetado para ler diferentes tipos de fontes de dados.

# EXPLORANDO O MÉTODO pandas.read_html()
# O método pandas.read_html() é utilizado para extrair tabelas de uma página web.
# Ele procura automaticamente por elementos HTML<table> na estrutura da página e retorna uma lista de DataFrames correspondentes às tabelas encontradas.
# Parâmetros como o 'io' podem ser configurados para especificar a URL da página a ser lida..
# Outros parâmetros adicionais podem ser ajustados para lidar com formatação e tratamento de dados.

# EXEMPLO - LER A URL DE UMA LISTA DE BANCOS DOS EUA QUE FALIRAM
import pandas as pd

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)

df_bancos.head()