import pandas as pd

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]})

df.to_csv('ob.csv')

read_csv = pd.read_csv("../ob.csv")
print(read_csv)

# HDF5
df.to_hdf("foo.h5", "df")


# Gravando em um arquivo Excel.

df.to_excel("foo.xlsx", sheet_name="Sheet1")
# Lendo de um arquivo do Excel.

pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])