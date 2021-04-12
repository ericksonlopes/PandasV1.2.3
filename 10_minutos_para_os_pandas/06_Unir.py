import numpy as np
import pandas as pd


# Concat

# Concatenar objetos pandas junto com concat():
df = pd.DataFrame(np.random.randn(10, 4))
print(df, '\n')

pieces = [df[: 3], df[3: 7], df[7:]]

print(pd.concat(pieces), '\n')

# Junte-se ¶
# O estilo SQL se funde. Veja a seção de junção de estilo de banco de dados .
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

print(left, '\n')
print(right, '\n')

# ligar chaves por key
print(pd.merge(left, right, on='key'))
print(pd.merge(right, left, on='key'))

