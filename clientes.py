import pandas as pd
import numpy as np 

df=pd.read_excel('clientes.xlsx')

print(df.head())

print(df.isnull().sum())

df=df.dropna(subset=['RFC'])

df=df.dropna(subset=['NOMBRE'])

print(df.isnull().sum())

#Viendo que se tenían dos columnas con nulos, pero que sin embargo el total de los 
#mismos no representaban un pocentaje importante del total de la data, además 
#no se recomienda tranformar valores conforme a los otros que se tiene cuando cada uno de ellos
#es único. 


