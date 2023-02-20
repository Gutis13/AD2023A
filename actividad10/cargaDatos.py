# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:19:09 2023

@author: erick
"""
#Nombre: Erick Gutiérrez Rubio 
#Código: 219284107 
#En este código se le cambiaron los nombres a los títulos
#en español,se acomodaron los nombres y datos en un archivo de excel
#se hicieron diferentes archivos con formatos diferentes 
#se cargaron datos 
#Fecha: 17/02/2023


import pandas as pd

fichero = 'C:\datos\precios_coches.csv' 

#datos = pd.read_csv(fichero, header=None)
datos = pd.read_csv(fichero)

#print(datos)
print(datos.head(5)) 
print('*'*10)
print(datos.tail(6))

print(datos.columns) 

titulos_cabecera=  ['indice','nombre','localizacion','año','kilometros recorridos','combustible','transmision','tipo propietario', 'kilometraje','motor', 'potencia', 'asientos','precio']

datos.columns = titulos_cabecera 
print(datos.head(5))
print(datos.columns)

#exportar datos
fichero = 'C:\datos\precios_cochesCopia.json' 
datos.to_csv(fichero) 

#otros formatos de archivos 
datos.to_json(fichero) 
#datos.to_excel(fichero) 
datos.to_sql(fichero) 

pd.read_json(fichero)  
#_excel(fichero)
#_sql(fichero) 
