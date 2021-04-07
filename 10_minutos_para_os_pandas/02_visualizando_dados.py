import numpy as np
import pandas as pd

dados = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col = ['a', 'b', 'c']
idx = ['a1', 'b2', 'c3']

df = pd.DataFrame(data=dados, index=idx, columns=col)

print(df, '\n')
# Veja como visualizar as linhas superior e inferior do quadro:
print(df.head(2), '\n')
print(df.tail(2), '\n')

# Exibir o índice, colunas:
print(df.index, '\n')

# nosso DataFramede todos os valores de ponto flutuante, DataFrame.to_numpy()é rápido e não requer a cópia de dados.
print(df.to_numpy(), '\n')

for item in df.to_numpy():
    print(item)

# describe() mostra um rápido resumo estatístico de seus dados:
print(df.describe(), '\n')

# Transpondo seus dados:
print(df.T, '\n')

# Classificando por eixo:
print(df.sort_index(axis=0, ascending=False), '\n')
print(df.sort_index(axis=1, ascending=False), '\n')

# Classificando por valores:
print('\n')
print('\n')
