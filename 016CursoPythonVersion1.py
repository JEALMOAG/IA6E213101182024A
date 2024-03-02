"""
Jesus Alejandro Montes Aguila 21310118
20 febrero 2024
Practica 51 - 54 y el capitulo 36
"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 51
#Definicion de funcion, def funcion(arg1,arg2,...,argn):\
    #num1 y num2 son argumentos que representan las variables con las que\
        # se estaran trabajando durante todo el programa
def suma(num1,num2):
    print("Resultado de suma: ", num1 + num2)
suma(8,22)
suma(35,15)
suma(50000,7000)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 52 "*args" argumentos arbitrarios, son aquellos que te permiten\
    # realizar una infinidad de argumentos tipo arreglo[i]
def colores(*args):
    print("Cantidad de argumentos: ", len(args))
colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 53
def colors (*args):
    print('El color', args[1],'es mi favorito.', 'El color',args[0],'tampoco esta mal.')
colors('rojo', 'naranja')
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 54
def suma2(*args):
    print("La suma de los 4 nuemros es: ",args[0] + args[1] + args[2] + args[3])
suma2(4,7,9,12)
#Capitulo 36
#Este capitulo consta de crear funciones con **kwards, el cual ayuda a\
#argumentos arbitrarios en diccionarios, ya que es permite entrar en las \
#dos partes de  los diccionarios.
def mascotas(m1,m2,m3,m4):#aqui empieza una funcion mascotas la cual es funcion con argumentos comunes 
    print("Esta mascota es:", m1 + ".") 
mascotas(m1= "perro", m2= "gato", m3= "canario", m4= "hamster" )#aqui termina una la funcion mascotas la cual es la funcion con argumentos comunes
def mascota(**kwargs):
    print("Esta mascota es:", kwargs["m3"] + ".")
mascota(m1= "perro", m2= "gato", m3= "canario", m4= "hamster" )
def addition(a,b):
    return a+b#resgresa el valor del resultado de la suma a+b
total = addition (3,4)
print(total)
def substraction(a,b):
    return a-b
total = substraction(23,13)
print(total)
def multiplication(a,b):
    return a*b
total = multiplication (5,6)
print(total)
def division(a,b):
    return a/b
total = division(56,13)
print(total)
