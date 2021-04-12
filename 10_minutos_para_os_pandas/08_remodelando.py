import numpy as np
import pandas as pd

tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)

print(tuples, '\n')

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

print(df, '\n')

df2 = df[:4]

# O stack()método “compacta” um nível nas colunas do DataFrame.
stacked = df2.stack()

print(stacked, '\n')
print(stacked.unstack(0), '\n')
print(stacked.unstack(1), '\n')

# Tabelas dinâmicas

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12), }
)

print(df, '\n')

# Podemos produzir tabelas dinâmicas a partir desses dados com muita facilidade:
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))