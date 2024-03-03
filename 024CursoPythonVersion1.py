"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 44
"""
#capitulo 44, funcion lamda e importacion libreria math
import math 
def area (radio):#definicion de una funcion area con argumento radio
    resultado = round(math.pi * radio**2,4)#math.pi es una clase la cual da el valor exacto de pi
    print(resultado)

area(2)

area = lambda radio:round(math.pi*radio**2,4)#simplifica funciones cortas, te ayuda a ahorrar lineas de codigo 
print(area(3))