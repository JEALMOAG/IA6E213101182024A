"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 41
"""
#practica 41 herencias de clases
#La herencia de clases sirve para ahorrar lineas de codigo, aprovechando al maximo cada metodo y atributo creado en la clase padre\
    #estos pueden ser utilizados al crear un clase hija con cualquier ciempre y cuendo tenga como parametro el nombre de la clase padre\
        # ejemplo class hija(padre), una vez creada la clase hija, a este se le puede agregar atributos y metodos completamente diferentes\
            # a los ya heredados.
class PCs():#se crea la clase padre
    def __init__(computer,name,processor):#se define el constructor con sus devidos Atributos
        computer.name = name
        computer.processor = processor
    
    def mostrarDatos(show):# se crea el metodo mostrar Datos
        print("El dispositivo es: " + show.name + " con procesador " + show.processor)
        
pc1 = PCs("LEGION","CORE i9") # se crea el objeto 
pc1.mostrarDatos()# el objeto ejecuta el metodo mostrar datos

class Tablets(PCs):# se crea la clase hija (clase que hereda)
    pass# en este caso de vacia con la palabra reservada pass

tablet1 = Tablets("IPAD AIR 5","M1") # se crea un objeto de la clase Tablets la cual ha heredado 
    # los metodos de la claase PCs tanto el constructor como el metodo mostrar datos
tablet1.mostrarDatos()# se usa el metodo de la clase padre mostrar datos 