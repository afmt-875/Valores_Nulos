import pandas as pd
df = pd.read_excel('precios_productos.xlsx')
print(df.isnull().sum())

df['NOMBRE_VENDEDOR'] = df['NOMBRE_VENDEDOR'].fillna('PÚBLICO EN GENERAL')
print(df.isnull().sum())

df.to_excel('precios_productos_clean.xlsx')
