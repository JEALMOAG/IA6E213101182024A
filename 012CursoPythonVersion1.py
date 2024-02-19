"""
Jesus Alejandro Montes Aguila 21310118
18 febrero 2024
Practica 28-35"""
print('\n\t"Practica 28"')#el metodo remove ayuda a eliminar un elemento de la lsita invocando su nombre
colores = ['rojo','azul','verde','amarillo','marron','lila','negro','rosa','blanco','naranja']
colores.remove('amarillo')
colores.remove('rojo')
print(colores)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\n\t"Practica 29"')#el metodo pop tambien elimina un elemento de la lista solo que este la elimina de acuerdo a la posicion 
colores1 = ['rojo','azul','verde','amarillo','marron','lila','negro','rosa','blanco','naranja']
valor = colores1.pop(1)
valor1 = colores1.pop(7)
array = [valor,valor1]
print(array)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\n\t"Practica 30"')#El metodo append agrega a la ultima posicion de la lista.
colores2 = ['rojo','azul','verde','amarillo','marron','lila','negro','rosa','blanco','naranja']
colores2.append('fuxia')
colores2.append('celeste')
print(colores2)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\n\t"Practica 31"')# El metdo insert permite agregar elementos a la lista de manera ordenada, ya que tu puedes escoger la posicion en la que ira el nuevo elemnto de la lista
colores3 = ['rojo','azul','verde','amarillo','marron','lila','negro','rosa','blanco','naranja']
colores3.insert(-4,'magenta')
colores3.insert(-1,'turquesa')
print(colores3)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\n\t"Practica 32"')#sort acomoda tu lista en orden alfabetico 
colores4 = ['rojo','azul','verde','amarillo','marron','lila','negro','rosa','blanco','naranja']
colores4.sort(reverse=True)#si se pone reverse=True el orden cambia de Z-A, y sin este el orden es A-Z.
print(colores4)
print("Longitud de la lista: ",len(colores4))#len(lista) ayuda a contar la cantidad de elementos de esta
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\n\t"Practica 33"')#las tuplas son muy parecidas a las listas, sin embargo, estas se escriben con parentesis y son inmutables  
tupla1 = ('rojo','azul','verde','amarillo','marron','lila','negro','rosa','blanco','naranja')
print(tupla1[1])
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\n\t"Practica 34"')
tupla2 = (10,1,5,11)
suma = tupla2[0]+tupla2[-1]+tupla2[2]-tupla2[1]
print(suma)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\n\t"Practica 35"')# tuple(lista) convierte una lista a tupla &&& list(tupla) convierte una tupla a lista      
colores5 = ['rojo','azul','verde','amarillo','marron','lila','negro','rosa','blanco','naranja']
colores5T = tuple(colores5)
print(type(colores5T))
