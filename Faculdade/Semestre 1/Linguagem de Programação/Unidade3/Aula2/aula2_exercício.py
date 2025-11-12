# USANDO A BIBLIOTECA PANDAS PARA DESCOBRIR O PÚBLICO-ALVO DE UMA LOJA, CALCULANDO A MÉDIA DE IDADE DOS CLIENTES

import pandas as pd

# Dicionário com nomes e idades
dados = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Idade': [25, 30, 22, 35, 28]
}

# Criando uma série a partir do dicionário
series_idades = pd.Series(dados['Idade'], index=dados['Nome'])

print('Série de Idades:')
print(series_idades)

# Calculando a média das idades
media_idades = series_idades.mean()
print('\nMádia de Idades:', media_idades)

