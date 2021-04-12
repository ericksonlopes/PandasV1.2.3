

# pandas podem incluir dados categóricos em a DataFrame. Para documentos completos,
#   consulte a introdução categórica e a documentação da API .
import pandas as pd

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]})

print(df, '\n')

# Converta as notas brutas em um tipo de dados categórico.
df["grade"] = df["raw_grade"].astype("category")

print(df["grade"], '\n')

# Renomeie as categorias com nomes mais significativos (a atribuição a Series.cat.categories()está em vigor!).
df['grade'].cat.categories = ['very good', 'good', 'very bad']
print(df["grade"], '\n')

df["grade"] = df["grade"].cat.set_categories( ["very bad", "bad", "medium", "good", "very good"])

print(df["grade"], '\n')

print(df.sort_values(by='grade'), '\n')

print(df.groupby("grade").size(), '\n')


