import pandas as pd
import numpy as np

dados = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col = ['c1', 'c2', 'c3']
idx = ['l1', 'l2', 'l3']

df = pd.DataFrame(data=dados, index=idx, columns=col)

# Selecionar uma única coluna, que produz um Series, equivalente a df.A:
print(df.c2, '\n')

# Selecionando via [], que corta as linhas.
print(df[0: 2], '\n')

print(df['l2': 'l3'], '\n')

# Seleção por rótulo
print(df.loc['l2'], '\n')


dates = pd.date_range("20130101", periods=6)
df1 = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'), index=dates)

print(df1)
# Exibir apenas o primeiro valor de dates (index)
print(df1.loc[dates[0]])

# Exibir apenas as colunas A B
print(df1.loc[:, ['A', 'B']], '\n')


# edução nas dimensões do objeto devolvido: dps do  20130102 exindo as colunas a e b
print(df1.loc['20130102':, ['A', 'B']], '\n')

# Redução nas dimensões do objeto devolvido:
print(df1.loc['20130102', 'A'], '\n')


# Seleção por posição

# Selecione por meio da posição dos inteiros passados:
print(df1.iloc[3], '\n')

# Por fatias inteiras, agindo de forma semelhante a numpy / Python:
print(df1.iloc[1:5, 0:2], '\n')

# Por listas de localizações de posições inteiras, semelhantes ao estilo NumPy / Python:
print(df1.iloc[[1, 2, 4], [0, 2]], '\n')

# Para fatiar linhas explicitamente:
print(df1.iloc[1:3, :], '\n')

# Para fatiar colunas explicitamente:
print(df1.iloc[:, 1:3], '\n')

# Para obter um valor explicitamente:
print(df1.iloc[1, 1], '\n')

# Para obter acesso rápido a um escalar (equivalente ao método anterior):
print(df1.iat[1, 1], '\n')

