import pandas as pd
import numpy as np


# Estatísticas

index_dt = ['A', 'B', 'C', 'D', 'E', 'F']
dates = pd.date_range("20130101", periods=6)
df = pd.read_csv('df2.csv', header=None, names=index_dt, index_col=0, sep=',')
df = df.dropna(how='any')

print(df.to_string(), '\n')
print(df.mean(), '\n')
print(df.mean(1), '\n')

# Operar com objetos que possuem dimensionalidade diferente e precisam de alinhamento.
# Além disso, o pandas transmite automaticamente ao longo da dimensão especificada
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)

# Aplicar

# Aplicação de funções aos dados:

# Retorna a soma cumulativa dos elementos ao longo de um determinado eixo.
print(df.apply(np.cumsum))


# Histograma
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)

# soma a quantidade de cada elemento
print(s.value_counts())


# Métodos de string
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

print(s.str.lower())
print(s.str.upper())
