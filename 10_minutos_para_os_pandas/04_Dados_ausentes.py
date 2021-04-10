import pandas as pd
import numpy as np

index_dt = ['A', 'B', 'C', 'D', 'E', 'F']
dates = pd.date_range("20130101", periods=6)
df = pd.read_csv('df2.csv', header=None, names=index_dt, index_col=0, sep=',')

print(df.to_string(), '\n')

# # A reindexação permite que você altere / adicione / exclua o índice em um eixo especificado. Isso retorna uma cópia dos dados.
# df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
#
# df1.loc[dates[0] : dates[1], "E"] = 1
#
# print(df1.to_string(), '\n')

# Para eliminar quaisquer linhas que contenham dados ausentes.
print(df.dropna(how='any'), '\n')

# Preenchendo dados ausentes.
print(df.fillna(value=5), '\n')

# Para obter a máscara booleana onde estão os valores nan.
print(pd.isna(df))
