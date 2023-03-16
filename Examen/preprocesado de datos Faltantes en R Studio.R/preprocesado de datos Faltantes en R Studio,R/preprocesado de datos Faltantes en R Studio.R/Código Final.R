dataset = read.csv('D:/9 Semestre/EXAMEN/Data.csv')

dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary= ifelse(is.na(dataset$Salary), 
                       ave(dataset$Salary, FUN = function(x) mean (x, na.rm= TRUE)),
                      dataset$Salary)  


dataset = read.csv('D:/9 Semestre/EXAMEN/Data.csv')
dataset$Country = factor (dataset$Country, levels = c("France", "Spain", "Germany"), 
                          labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased, levels = c("No", "Yes"), 
                           labels = c(0,1)) 

dataset = read.csv('D:/9 Semestre/EXAMEN/Data.csv')
library(caTools) 
set.seed(123) 
split = sample.split(dataset$Purchased, SplitRatio =0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE) 

