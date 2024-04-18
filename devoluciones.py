import pandas as pd
df = pd.read_excel('devoluciones.xlsx')
print(df.isnull().sum())

# Para que el dataframe siga teniendo el mismo tipo de valores en esta columna he decidido inputar una fecha que simplemente no tenga sentido 
df['FECHA_CANCELA'] = df['FECHA_CANCELA'].fillna(pd.to_datetime('1900-01-01'))
print(df.isnull().sum())

df['CVE_PEDI'].fillna(df['DOC_ANT'], inplace=True)
df['DOC_ANT'].fillna(df['CVE_PEDI'], inplace=True)
print(df.isnull().sum())

df['CVE_VEND'] = df['CVE_VEND'].fillna(0)
print(df.isnull().sum())

df.to_excel('devoluciones_clean.xlsx')