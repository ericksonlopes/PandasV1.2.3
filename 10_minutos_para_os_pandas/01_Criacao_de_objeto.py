import numpy as np
import pandas as pd

# Criação de valores nulos
print(np.nan, '\n')

# Criar um Series passando uma lista de valores, permitindo que os pandas criem um índice inteiro padrão:

dados = [1, np.nan, 5, np.nan] + [num for num in range(5)]

s = pd.Series(dados)
print(s, '\n')

# Criando um DataFrame passando uma matriz NumPy, com um índice datetime e colunas rotuladas:

# Criando datas
dates = pd.date_range('20210407', periods=6)

print(dates, '\n')

# criando matriz de valores com 6 linhas e quatro colunas
print(np.random.randn(6, 4), '\n')

# colocando as dates como index e uma lista com ABCD como colunas
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df, '\n')


dados = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col = ['a', 'b', 'c']
idx = ['a1', 'b2', 'c3']

df2 = pd.DataFrame(data=dados, index=idx, columns=col)
print(df2, '\n')

print(df2.dtypes, '\n')

print(df2.T)
