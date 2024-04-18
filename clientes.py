import pandas as pd
import numpy as np

df = pd.read_excel('clientes.xlsx')
print(df.isnull().sum())

df['RFC'] = df['RFC'].fillna('XAXX010101000')
df['NOMBRE'] = df['NOMBRE'].fillna('John Doe')
print(df.isnull().sum())

df.to_csv('clientes_clean.csv')