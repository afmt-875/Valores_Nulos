import pandas as pd
df = pd.read_excel('notas_credito.xlsx')
print(df.isnull().sum())


df['FECHA_CANCELA'] = df['FECHA_CANCELA'].fillna(pd.to_datetime('1900-01-01'))
df['CVE_PEDI'] = df['CVE_PEDI'].fillna('F00000')
df['CVE_VEND'] = df['CVE_VEND'].fillna(0)

print(df.isnull().sum())

df.to_excel('notas_credito_clean.xlsx')