#Plantilla para el Pre Procesado de Datos = Datos categóricos 
#Importar el dataset 
dataset = read.csv('C:/Examen Analitica/Data.csv' , stringsAsFactors = F)

str(dataset)

dataset = read.csv('D:/9 Semestre/EXAMEN/Data.csv')
#Codificar las variables categóricas
dataset$Country = factor (dataset$Country, levels = c("France", "Spain", "Germany"), 
                          labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased, levels = c("No", "Yes"), 
                           labels = c(0,1)) 
str(dataset) 