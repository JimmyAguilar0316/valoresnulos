import pandas as pd
import numpy as np 

df=pd.read_excel('devoluciones.xlsx')

print(df.head())

print(df.isnull().sum())


columnas= ['FECHA_CANCELA', 'DOC_ANT', 'CVE_VEND', 'CVE_PEDI']

df[columnas] = df[columnas].fillna({'FECHA_CANCELA': '--', 'DOC_ANT': '--', 'CVE_VEND': '--', 'CVE_PEDI': '--'})

valores_nulo = df.isnull().sum()
print(valores_nulo)

#En este caso, vemos que el dataset que tenemos, nos da valores unicos de las devoluciones. en este caso, se pusieron guiones 
#en donde había nulos ya que, no queremos sacar la media de datos que son únicos y se consideran muchos para eliminar el registro por completo 
