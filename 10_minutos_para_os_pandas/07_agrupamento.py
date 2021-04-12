import pandas as pd
import numpy as np

df = pd.DataFrame(
       {
           "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
           "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
           "C": np.random.randn(8),
           "D": np.random.randn(8),
       }
   )

print(df, '\n')

# Agrupando e aplicando a sum()função aos grupos resultantes.
print(df.groupby("A").sum())
print(df.groupby("B").sum())

# O agrupamento por várias colunas forma um índice hierárquico e, novamente, podemos aplicar a sum() função.
print(df.groupby(['A', 'B']).sum())

