#Erick Gutiérrez Rubio 
# Código: 219284107 
# 1er Evaluación Practica Parte II
#Plantilla para el Pre Procesado de Datos
#Importar el dataset 
dataset = read.csv('C:/Examen Analitica/Data.csv')
#dataset = dataset[2:3] 

#Dividir los datos en conjunto de entrenamiento y conjunto de test
#install.packages("caTools") 
dataset = read.csv('D:/9 Semestre/EXAMEN/Data.csv')
library(caTools) 
set.seed(123) 
split = sample.split(dataset$Purchased, SplitRatio =0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE) 

