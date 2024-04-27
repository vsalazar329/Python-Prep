#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
x = -1
if x<0:
    print("El numero", x, "es menor a cero.")
elif x>0:
    print("El numero", x, "es mayor a cero.")
else:
    print("El numero", x, "es igual a cero.")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
var1 = "Dinero"
var2 = '15'

if type(var1) == type(var2):
    print("Las variables son del mismo tipo.")
else:
    print("Las variables son de distintos tipos.")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for i in range(1, 21):
    if i%2 == 0:
        print(i, "es par.")
    else:
        print(i, "es impar")




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(6):
    print(i**3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
x = 8
for i in range(x):
    pass
print(i)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

n = 10
if (type(n) == int):
    if n > 0:
        factorial = n
        while n > 2:
            n = n - 1
            factorial = factorial*n
        print("El factorial es", factorial)
    else: 
        print("La variable no es mayor que cero")
else:
    print("La variable no es un entero.")




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

n = 10
m = 2
while n > 0:
    n = n -1
    for i in range(m):
        print("Marico el que lo lea")



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
n = 4
for i in range(1, n):
    while 0 < n < 5:
        n = n-1
        print("Ciclo while nro", n)
        print("Ciclo for nro"




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
top = 30
n = 0
primo = True
while n < top:
    for div in range(2, n):
        if n%div == 0:
            primo = False
    if primo:
        print(n)
    else:
        primo = True
    n += 1


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

top = 30
n = 0
primo = True
while n < top:
    for div in range(2, n):
        if n%div == 0:
            primo = False
            break
    if primo:
        print(n)
    else:
        primo = True
    n += 1



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
top = 30
n = 0
primo = True
ciclos_sin_break = 0

while n < top:
    for div in range(2, n):
        ciclos_sin_break += 1
        if n%div == 0:
            primo = False
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print('Numero de ciclos', ciclos_sin_break)



# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:





# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

top = 30
n = 0
primo = True
ciclos_con_break = 0
while n < top:
    for div in range(2, n):
        ciclos_con_break += 1
        if n%div == 0:
            primo = False
            break
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print('Numero de ciclos', ciclos_con_break)
print("Se mejoro en", ciclos_con_break/ciclos_sin_break)


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

n = 99
while n <= 300:
    n += 1
    if n%12 != 0:
        continue
    else:
        print(n, "es divisible por 12")

