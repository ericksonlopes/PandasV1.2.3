import pandas as pd

d = {str(item): num for item, num in
     enumerate(['Sr. Murilo Barbosa', 84, 'barbosabernardo@bol.com.br', '+55 84 9718-3772'])}

print(d, '\n')

# Construindo séries de um dicionário com um índice especificado
serie = pd.Series(d)

print(serie, '\n')

serie2 = pd.Series(data=d, index=['0', '1', '2', '3'])
print(serie2, '\n')

# As chaves do dicionário correspondem aos valores de Índice, portanto, os valores de Índice não têm efeito.
serie3 = pd.Series(data=d, index=['x', 'y', 'z'])
print(serie3, '\n')

