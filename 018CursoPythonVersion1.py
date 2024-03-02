"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 38
"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#capitulo 38 metodo __init__ se utiliza como constructor si compramos con el lenguage \
    # de porgramacion c o cpp, donde se definien atributos iniciales por default, \
        # en este codigo el nombre y pin del usuario son atributos inciales para el constructor de mi objeto. 
class usuarios():
    def __init__(self,nombre,pin):#se fenien los atributos inciales nombre y pin 
        self.nombre = nombre# el nombre se declara en cada objeto creado.
        self.pin = pin # el pin se declara en cada objeto creado
    def saludo(self):#metodo saludo
        print("Saludos " + self.nombre + ". Iniciaste sesion correctamente.")
    def mostrarPin(self):# metodo mostrar el pin
        print("Tu pin es: "+self.pin)
    def despedida(self):# metodo despedit
        print(self.nombre + ", cerraste la sesion")

usuario1 = usuarios("Jesus","2306")#se crea el objeto 1
usuario2 = usuarios("Victoria","2509")# se crea el objeto 2

usuario1.saludo()#objeto implenta el metodo saludo de la clase usuarios 
PIN = input("Olvidaste tu pin??? SI-1 NO-0\n")
if (PIN == '1'):
    usuario1.mostrarPin()
else:
    usuario1.despedida()

usuario2.saludo()
PIN = input("Olvidaste tu pin??? SI-1 NO-0\n")
if (PIN == '1'):
    usuario2.mostrarPin()
else:
    usuario2.despedida()

