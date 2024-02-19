"""
Jesus Alejandro Montes Aguila 21310118
19 febrero 2024
Practica 36-41"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 36 hacer que la condicon sea True
num1 = 15
num2 = 20
if num1 < num2:
    print('Se ejecuta el if.')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 37 hacer que la condicon sea True
num3 = 1450
num4 = 60
if num3 > num2:
    print('Se ejecuta el if.')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 38 hacer que la condicon sea False
num3 = 1450
num4 = 60
if num3 == num2:
    print('Se ejecuta el if.')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 39 corregir el siguiente condicional
color = 'rojo'
if color != 'rojo':
    print("El color no es rojo")
else:
    print("El color es rojo")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 40 Agregar un rago de edad 18-45 años y 100-120
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
    print('Nadie puede tener esa edad')
elif edad < 18:
    print('Eres menor de edad')
elif edad <45:
    print('Eres un adulto joven')
elif edad <= 120:
    print('Eres un adulto mayor')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 41 buscar en una lista o tupla in lista o un tupla
colores = ('verde','rojo','azul','naranja')
color = input("\nEscriba su color favorito\n")
if color in colores:# la condicion evalua si el color tecleado por el usuario se encuentra en la tupla gracias al "in" varibale in lista
    print("El color se encuentra en la tupla")
else:
    print("Lo lamento, el color no se encuentra en la tupla")
    

    

           
