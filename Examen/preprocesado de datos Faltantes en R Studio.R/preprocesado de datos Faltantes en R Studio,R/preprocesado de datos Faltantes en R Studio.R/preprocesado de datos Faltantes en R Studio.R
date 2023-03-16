#Plantilla para el Pre Procesado de Datos = Datos faltantes 
#Importar el dataset 
dataset = read.csv('D:/9 Semestre/EXAMEN/Data.csv')

#Tratamiento de los valores N/A 
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary= ifelse(is.na(dataset$Salary), 
                       ave(dataset$Salary, FUN = function(x) mean (x, na.rm= TRUE)),
                      dataset$Salary)  
