#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
num = 34
print(num)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
num2 = 8.5
print(type(num2))


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(num))


# 4) Crear una variable que contenga tu nombre

# In[2]:
nombre = "Juan Manuel Otálora Hernández"


# 5) Crear una variable que contenga un número complejo

# In[3]:
num3 = 23 + 5j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(num3))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:

pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

valor = True
valor2 = 10 > 5


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(valor))
print(type(valor2))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
suma = 5+12.34


# 11) Realizar una operación de suma de números complejos

# In[2]:

suma2 = 52.9999 + 3j + 0.66666+1j


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
suma3 = 7+34+9j
print(type(suma3))

# 13) Realizar una operación de multiplicación

# In[5]:
mul = 3*3


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
potencia = 2**8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente = 27/4
print(cociente)


# 16) De la división anterior solamente mostrar la parte entera

# In[9];
parte_entera = 27//4


# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
resto = 27 % 4


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
resultado = (4*parte_entera)+resto


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
texto = "hola " + "como estás?"


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
num4 = 2
num5 = "2"
evaluacion = num4 == num5


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
num6 = int(num5)
evaluacion2 = num4 == num6


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]: Por que Python no reconoce la coma, para definir los números decimales

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
variable = 3
variable -= 1

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
num7 = 1 << 5
print(num7)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
op = 2+"2"

# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
op2 = "hola "*3
