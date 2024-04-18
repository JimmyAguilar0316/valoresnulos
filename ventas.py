import pandas as pd
import numpy as np 

df=pd.read_csv('ventas_totales.csv')
print(df.head())

print(df.info())

print(df.describe())

#print(df.isnull().sum())


df['salon_ventas']=df['salon_ventas'].fillna( round(df.salon_ventas.mean(),1))
valores_nulo=df.isnull().sum()
#print(valores_nulo)

df.tarjetas_credito=df.tarjetas_credito.fillna( round(df.tarjetas_credito.mean(),1)) 
valores_nulo=df.isnull().sum()
print(valores_nulo)

