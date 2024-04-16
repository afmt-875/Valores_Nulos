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
#print(df.isnull().sum())

#quitar nulos de otros medios
df['otros_medios']=df['otros_medios'].fillna(6922148.759)
#print(df.isnull().sum())

# rellena valores nulos con metodo ffill
df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
#print(df.isnull().sum())

# rellena valores nulos con metodo bfill
df['almacen'] =df['almacen'].fillna(method='bfill')
#print(df.isnull().sum())

# rellena con ceros la columna panaderia
df['panaderia'] =df['panaderia'].fillna(0)
#print(df.isnull().sum())

#Convertir DataFrame a CSV
df.to_csv('ventas_totales_limpio.csv')