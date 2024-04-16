import pandas as pd
import numpy as np

df = pd.read_csv('ventas_totales.csv')
#print(df.isnull().sum())

#quitar nulos en la columna salon_ventas 
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
#print(df.isnull().sum())

#quitar nulos tarjeta de debito
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
#print(df.isnull().sum())

#quitar nulos tarjeta de credito
df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
print(df.isnull().sum())