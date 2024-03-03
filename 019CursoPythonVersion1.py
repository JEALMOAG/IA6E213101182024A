"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 39
"""
#Capitulo 39 consta de modifcar los valores iniciales de mi constructor __init__ una vez \
    #capturados. Tambien del uso de los self que se encuentran definidos en los metodos.
class usuarios():
    def __init__(self,nombre,edad):#se fenien los atributos inciales nombre y edad
        self.nombre = nombre# el nombre se declara en cada objeto creado.
        self.edad = edad # la edad se declara en cada objeto creado
        
    def muestraDatos(self):#cada self de cada metodo es diferente uno de otro. Y posible cambiarle el nombre.
        print("El nombre del usuario es: "+  self.nombre,self.edad)
            
usuario1 = usuarios("Jesus",25)
usuario1.muestraDatos()
usuario1.edad = 20#Se hace una correcion de datos de mi constructor.
usuario1.muestraDatos()
class usuarios():
    def __init__(datosPersonales,nombre,edad):#se fenien los atributos inciales nombre y edad pero con atributo datosPersonales en vez del self
        datosPersonales.nombre = nombre# el nombre se declara en cada objeto creado pero ahora utilizando datosPersonales.1erAtributo
        datosPersonales.edad = edad # la edad se declara en cada objeto creado
        
    def muestraDatos(show):#se implenta un self diferente, yo lo llame show, y de esta manera invocare a mis Atributos dentro de mi metodo y posteriormente\
        #en los objetos.
        print("El nombre del usuario es: "+  show.nombre,show.edad)
            
usuario2 = usuarios("Victoria",22)#se crea el segundo objeto
usuario2.muestraDatos()
usuario2.edad = 19
usuario2.muestraDatos()