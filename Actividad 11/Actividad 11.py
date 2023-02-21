#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Erick Gutiérrez Rubio 
#Código: 219284107
#20/02/2023
#Actividad 11 Analítica de Datos 2023-A LTIN
print("Hello World")


# In[2]:


"Hello world"


# In[3]:


# la funcion type nos permite ver el tipo de dato de un objeto 
type(1) 


# In[4]:


type(2.3)


# In[5]:


1 + 2


# In[6]:


3 ** 2


# In[7]:


type(True)


# In[8]:


type("Hello World")


# In[9]:


# cambiar miniscula, mayuscula, etc
print("Hello World".upper()) 
print("Hello World".lower()) 
print("hello world".title()) 

#contar letras
print("hello world".count('l'))
# reemplazar letras de cadenas de texto 
print("hello world".replace('o','u'))


# In[10]:


message_1= "Estoy aprendiendo Python"


# In[11]:


message_1


# In[12]:


message_2 = "y es divertido!"


# In[13]:


message_2


# In[14]:


message_1 + message_2


# In[15]:


message_1+ " " + message_2


# In[16]:


message = f' {message_1} {message_2}' 
message


# In[20]:


countries = ['United States', 'India', 'China', 'Brazil']


# In[21]:


countries


# In[22]:


countries[0]


# In[23]:


countries[1]


# In[24]:


countries[3]


# In[25]:


countries[-1]


# In[26]:


countries[-4]


# In[27]:


countries


# In[28]:


countries[0:3]


# In[29]:


countries[1:]


# In[30]:


countries[:2]


# In[31]:


countries


# In[32]:


countries.append('Canada')


# In[33]:


countries


# In[34]:


countries.insert(0,'Argentina')


# In[35]:


countries


# In[36]:


countries_2 = ['UK', 'Alemania', 'Australia']


# In[37]:


countries + countries_2


# In[38]:


nueva_lista = [countries, countries_2]


# In[39]:


nueva_lista


# In[40]:


countries.remove('Canada')


# In[41]:


countries


# In[42]:


countries.pop(0)


# In[43]:


countries


# In[44]:


del countries[0]


# In[45]:


countries


# In[46]:


numbers = [4,3,10,7,1,2]


# In[47]:


numbers


# In[48]:


numbers.sort()


# In[49]:


numbers


# In[50]:


numbers.sort(reverse=True)


# In[51]:


numbers


# In[52]:


numbers[0]=1000


# In[53]:


numbers


# In[54]:


countries.append('Argentina')


# In[55]:


countries


# In[56]:


nueva_lista_3= countries


# In[57]:


nueva_lista_3


# In[58]:


nueva_lista = countries.copy()


# In[60]:


nueva_lista


# In[61]:


nueva_lista_2 = countries[:]


# In[62]:


nueva_lista_2 


# In[63]:


mi_diccionario = {'key1':'value1','key2':'value2'}


# In[64]:


my_data = {'nombre':'Frank','edad':26}


# In[65]:


my_data


# In[66]:


my_data['nombre']


# In[67]:


my_data.keys()


# In[68]:


my_data.values()


# In[69]:


my_data.items()


# In[70]:


my_data = {'nombre':'Frank','edad' :26}


# In[71]:


my_data['estatura']=1.7


# In[72]:


my_data


# In[73]:


my_data.update({'estatura':1.9, 'languages':['Ingles','Español']})


# In[74]:


my_data


# In[75]:


nuevo_diccionario = my_data.copy()


# In[76]:


nuevo_diccionario


# In[77]:


my_data


# In[78]:


my_data.pop('estatura')


# In[79]:


my_data


# In[80]:


del my_data['languages']


# In[81]:


my_data


# In[82]:


my_data.clear()


# In[83]:


my_data


# In[84]:


edad = 24 

if edad>=18: 
    print("Eres mayor de edad")
elif edad>=13: 
    print("Eres un adolescente") 
else: 
     print("Eres un niño")


# In[85]:


countries = ['United States','India','China','Brazil']


# In[87]:


if "Colombia" in countries: 
    print("Pais está en la lista")
else: 
     print("Pais NO está en la lista")


# In[88]:


for pais in countries:
    print (pais)


# In[89]:


for pais in countries:
    if pais == "United States": 
        print(pais) 


# In[90]:


for numero, pais in enumerate(countries): 
    print(numero) 
    print(pais) 


# In[91]:


my_data = {'nombre':'Frank', 'edad':26}


# In[92]:


my_data


# In[93]:


my_data.items()


# In[94]:


for key, value in my_data.items():
    print(key)
    print(value) 


# In[95]:


countries


# In[96]:


len(countries)


# In[97]:


max([16, 83, 32, 1, 10])


# In[98]:


min([16, 83, 32, 1, 10])


# In[99]:


type(countries)


# In[100]:


type(my_data)


# In[101]:


round(2.333, 2) 


# In[102]:


for i in range(1, 10, 2): 
    print(i) 


# In[109]:


def sumar_numeros(a, b): 
    suma_final = a + b 
    return suma_final 


# In[110]:


sumar_numeros(10, 5)


# In[111]:


import os


# In[112]:


os.getcwd()


# In[113]:


os.listdir()


# In[114]:


os.makedirs("Nueva Carpeta") 


# In[115]:


os.listdir()


# In[ ]:




