import pandas as pd
import numpy as np 

df=pd.read_excel('precios_productos.xlsx')

print(df.head())

#print(df.isnull().sum())

df=df.dropna(subset=['NOMBRE_VENDEDOR'])
print(df.isnull().sum())

#Vemos que este dataframe posee solamente una columna con nulos 
# y a su vez, vemos que solamente tine dos registros con nulos, 
#por lo que se decide a eliminar esas dos filas. No se considera 
#que tenga una gran afectación esta acción. 


