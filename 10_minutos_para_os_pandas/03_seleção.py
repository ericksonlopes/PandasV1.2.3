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

# Indexação booleana

# Usando os valores de uma única coluna para selecionar dados.
print(df1[df1['A'] > 1], '\n')

# Seleção de valores de um DataFrame onde uma condição booleana é atendida.
print(df1[df1 > 0])


# Usando o isin()método de filtragem:
df2 = df1.copy()

df2['E'] = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis']

print(df2, '\n')

print(df2[df2["E"].isin(['dois', 'quatro'])], '\n')

# Ambiente

# Definir uma nova coluna alinha automaticamente os dados pelos índices.
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

print(s1, '\n')

df2['F'] = s1

print(df2, '\n')

# Definindo valores por rótulo:
df2.at[dates[0], 'A'] = 0

print(df2, '\n')

# Definindo valores por posição:

df2.iat[0, 1] = 0

print(df2, '\n')

# Configurando atribuindo com uma matriz NumPy:
df2.loc[:, 'D'] = np.array([5] * len(df2))

print(df2, '\n')

print(df2.index)
df2.to_csv('df2.csv', sep=',')

