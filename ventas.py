import pandas as pd
import numpy as np 

df=pd.read_csv('ventas_totales.csv')
print(df.head())

print(df.info())

print(df.describe())

#print(df.isnull().sum())


df['salon_ventas']=df['salon_ventas'].fillna( round(df.salon_ventas.mean(),1))
valores_nulo=df.isnull().sum()
print(valores_nulo)
#En este caso, decidí rellenar los nulos de la columna por la media, debido a que eran varios datos nulos. 

df.tarjetas_credito=df.tarjetas_credito.fillna( round(df.tarjetas_credito.mean(),1)) 
valores_nulo=df.isnull().sum()
print(valores_nulo)
#Con esta columna, es el mismo caso, por la cantidad de datos, decido remplazar los valores con la media. 

df.tarjetas_debito =df.tarjetas_debito .fillna( round(df.tarjetas_debito.mean(),1))
valores_nulo=df.isnull().sum()
#print(valores_nulo)
#Aunque en este caso, haya pocos nulos, debido a que se considera un método excelente, se realiza el mismo método. 

print(df.otros_medios.describe())

df['otros_medios']=df['otros_medios'].fillna(6922148.759)
valores_nulos=df.isnull().sum()
print(valores_nulos)
#Ahora, tratamos de usar una forma diferete de remplazar el único valor que tenemos, estolo hacemos, coclovando manualmente el valor de media. 

df['subtotal_ventas_alimentos_bebidas']=df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
print(valores_nulos)
#En este caso, se decidió hacer uso de otro método el cual nos llena los datos con los úlitmos valores que se tienen. Se quiso probar este método para probar diferentes efectividades.

print(df.bebidas.describe())

df['bebidas']=df['bebidas'].fillna(8878731)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Hacemos uso del método de llenar el valor con la media debido a que solo es un valor el faltante. 


df[['lacteos','panaderia','carnes','verduleria_fruteria','alimentos_preparados_rotiseria']] =df[['lacteos','panaderia','carnes','verduleria_fruteria','alimentos_preparados_rotiseria']].fillna(round(df[['lacteos','panaderia','carnes','verduleria_fruteria','alimentos_preparados_rotiseria']].mean(),1))
valores_nulo=df.isnull().sum()
print(valores_nulo)

#Realizamos el reemplazo de las siguientes varaibles conforme a la media, pensando en que eran pocos valores, se consideró mejor esta opción. 

df[['almacen','indumentaria_calzado_textiles_hogar','electronicos_articulos_hogar','otros']]=df[['almacen','indumentaria_calzado_textiles_hogar','electronicos_articulos_hogar','otros']].fillna(method='ffill')
valores_nulos=df.isnull().sum()
print(valores_nulos)
#Finalmente, para estas variables, al tener mas de un valor nulo, se lleva a cabo el reempalzo de los nulos con el método que repite los últimos valores. 