"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 40
"""
#capitulo 40, creacion de clases vacias, borrado de atributos del contructor y \
    #borrado de objetos.
class microprocesador():
    pass#la reservada pass ayuda a crear clases vacias (sin atributos ni metdos)

class PCs():
    def __init__(pc,name,processor):
        pc.name=name
        pc.processor=processor
    def muestraDatos(show):
        print("El tipo de computadora es: " + show.name,show.processor)

pc1 = PCs("Legion","CORE i7")
del pc1.processor # se borra el argumento procesador de mi objeto pc1
del pc1# se borra completamente todo el objeto. 
pc1.muestraDatos()# deberia de marcar un error, ya que no existe el objeto pc1.