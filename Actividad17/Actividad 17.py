# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:24:24 2023

@author: erick
"""

#Regresión Lineal Simple Modelo de Entrenamiento 
#Erick Gutiérrez Rubio
#8 de Marzo de 2023
#Analítica de Datos 

#Importar las librerias numpy, matploitlb y pandas

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

#importar el data set 
dataset = pd.read_csv('C:/Actividad17/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 1/3, random_state = 0) 

#Crear modelo de Regresión Lineal Simple con el conjunto de entrenamiento 
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train) 

#Predecir el conjunto de test
y_pred= regression.predict(X_test) 

#Visualizar los resultados de entrenamiento 
plt.scatter(X_train, y_train, color = "red") 
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Años de Experiencia Erick Gutiérrez Rubio")
plt.ylabel("Sueldo (en $)")
plt.show() 

# Visualizar los resultados de test 
plt.scatter(X_test, y_test, color = "red") 
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing)")
plt.xlabel("Años de Experiencia Erick Gutiérrez Rubio")
plt.ylabel("Sueldo (en $)")
plt.show() 


