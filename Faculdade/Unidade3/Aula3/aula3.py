# INTRODUÇÃO A MANIPULAÇÃO DE DADOS EM PANDAS

# O foco da biblioteca pandas é a manipulação de dados
# Dados de diverssas fonte: arquivos, páginas web, APIs, outros softwares, serviços de armazenamento em nuvem e bancos de dados
# O pandas oferece uma variedade de métodos que permitem a leitura e o carregamento desses dados em estruturas chamadas DataFrames
# Esses métodos de leitura têm em comum o prefixo 'pd.read_xxxx'
# 'pd' é um alias frequentemente utilizado ao importar a biblioteca
# Além da leitura, o pandas vários métodos para escrever os dados contidos em um DataFrame em arquivos, bancos de dados e áreas de transferência do sistema operacional

# A lista abaixo mostra os métodos de leitura e escrita para os diferentes tipos de dados:
'''
Descrição do Dado: CSV
Tipos de Dado: Texto
Método para Leitura: read_csv
Método para Escrita: to_csv

Descrição do Dado: Pipe-width Text
Tipos de Dado: Texto
Método para Leitura: read_table
Método para Escrita: to_table

Descrição do Dado: JSON
Tipos de Dado: Texto
Método para Leitura: read_json
Método para Escrita: to_json

Descrição do Dado: HTML
Tipos de Dado: Texto
Método para Leitura: read_html
Método para Escrita: to_html

Descrição do Dado: LaTeX
Tipos de Dado: Texto
Método para Leitura: read_latex
Método para Escrita: styler.to_latex

Descrição do Dado: XML
Tipos de Dado: Texto
Método para Leitura: read_xml
Método para Escrita: to_xml

Descrição do Dado: Local Clipboard
Tipos de Dado: Texto
Método para Leitura: read_clipboard
Método para Escrita: to_clipboard

Descrição do Dado: Excel
Tipos de Dado: Binário
Método para Leitura: read_excel
Método para Escrita: to_excel

Descrição do Dado: MS Access
Tipos de Dado: Binário
Método para Leitura: read_access
Método para Escrita: to_access

Descrição do Dado: OpenDocument
Tipos de Dado: Binário
Método para Leitura: read_ods
Método para Escrita: to_ods

Descrição do Dado: HDF5 Format
Tipos de Dado: Binário
Método para Leitura: read_hdf
Método para Escrita: to_hdf

Descrição do Dado: Feather Format
Tipos de Dado: Binário
Método para Leitura: read_feather
Método para Escrita: to_feather

Descrição do Dado: Parquet Format
Tipos de Dado: Binário
Método para Leitura: read_parquet
Método para Escrita: to_parquet

Descrição do Dado: ORC Format
Tipos de Dado: Binário
Método para Leitura: read_orc
Método para Escrita: to_orc

Descrição do Dado: MsgPack
Tipos de Dado: Binário
Método para Leitura: read_msgpack
Método para Escrita: to_msgpack

Descrição do Dado: Stata
Tipos de Dado: Binário
Método para Leitura: read_stata
Método para Escrita: to_stata

Descrição do Dado: SAS
Tipos de Dado: Binário
Método para Leitura: read_sas
Método para Escrita: to_sas

Descrição do Dado: SPSS
Tipos de Dado: Binário
Método para Leitura: read_spss
Método para Escrita: to_spss

Descrição do Dado: Pickle
Tipos de Dado: Binário
Método para Leitura: read_pickle
Método para Escrita: to_pickle

Descrição do Dado: SQL
Tipos de Dado: SQL
Método para Leitura: read_sql
Método para Escrita: to_sql

Descrição do Dado: Google BigQuery
Tipos de Dado: SQL
Método para Leitura: read_gbq
Método para Escrita: to_gbq
'''

# -- CAPTURA E TRANSFORMAÇÃO DOS DADOS --

# A etapa de captura e transformação/padronização dos dados é crucial no processo de análise de dados e modelagem de machine learning
# Nessa fase se coleta os dados brutos de várias fontes, como arquivos CSV, bancos de dados, APIs e os prepara para uma análise posterior
# Por ser uma biblioteca que fornece estruturas de dados flexíveis e ferramentas para manipular e transformar dados, o pandas é muito útil para essas tarefas

# EXEMPLO
'''
import pandas as pd

df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')
print(df_selic.info())
'''

# ESSE EXEMPLO DEU ESSE ERRO
# 01 DE OUTUBRO DE 2025 | NÃO CONSIGO RESOLVER

# SUPOSTO RESULTADO
'''
#resultado
<class 'pandas.core.frame.DataFrame'>

RangeIndex: 9379 entries, 0 to 9378

Data columns (total 2 columns):

 #   Column  Non-Null Count  Dtype 

---  ------  --------------  ----- 

 0   data    9379 non-null   object

 1   valor   9379 non-null   float64

dtypes: float64(1), object(1)

memory usage: 146.7+ KB

None
'''