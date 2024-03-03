"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 42
"""
# Capitlo 42 heredar propiedad __init__ 
# Para heredar la propidad __init__ se necesita definir un segundo init en la clase hija \
    #variable computer y va a comenzar a pasar los valor como argumento a los atributos del\
        #objeto ejemplo __init__(tableta,name,processor,3erAtributo) se agrega una segunda instruccion \
            # CLASE1.__init__(tableta,A1,A2,...,An) donde A1 son los atributos que queremos heredar.
class PCs():
    def __init__(computer,name,processor):
        computer.name = name
        computer.processor = processor
    
    def mostrarDatos(show):
        print("El dispositivo es: " + show.name + " con procesador " + show.processor)
        
pc1 = PCs("LEGION","CORE i9") 
pc1.mostrarDatos()

class Tablets(PCs):#clase hija 
    def __init__(tableta,name,processor,storage): #2do init y se agrega un 3er Atributo
        PCs.__init__(tableta,name,processor)# se espcifica los atributos que el nuevo init heredara
        tableta.storage = storage #se define los Atributos nuevos.
    def mostrarDatos(show2):# se crea un metodo para mostrar los datos actualizados de la segunda clase
        print("El dispositivo es:  "+ show2.name + " con procesador " + show2.processor + " y almacenamiento " + show2.storage)

tablet1 = Tablets("IPAD AIR 5","M1","256Gb") 
tablet1.mostrarDatos()