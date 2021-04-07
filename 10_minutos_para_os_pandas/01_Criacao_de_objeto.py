import numpy as np
import pandas as pd

# Criação de valores nulos
print(np.nan)

# Criar um Series passando uma lista de valores, permitindo que os pandas criem um índice inteiro padrão:

dados = [1, np.nan, 5, np.nan] + [num for num in range(5)]

s = pd.Series(dados)
print(s)

# Criando um DataFramepassando uma matriz NumPy, com um índice datetime e colunas rotuladas: