import pandas as pd
import numpy as np 

df=pd.read_excel('notas_credito.xlsx')

print(df.head())

print(df.isnull().sum())


columnas= ['CVE_VEND', 'CVE_PEDI', 'FECHA_CANCELA']

df[columnas] = df[columnas].fillna({'CVE_VEND': '--', 'CVE_PEDI': '--', 'FECHA_CANCELA': '--'})

valores_nulo = df.isnull().sum()
print(valores_nulo)

#Como con la base de datos de 'Devoluciones', en este caso, se decide hacer uso de los guiones para sustituir los datos 
#nulos que tenemos, esto para tratar de alterar lo menos posible el resultado de las operaciones
#que se puedan llegar a hacer con estos datos. 