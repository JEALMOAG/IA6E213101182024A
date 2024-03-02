"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 37
"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#capitulo 37

class Naves():#se crea la clase con el la palabra reservada class NOMBRE():
    peso = 2500#INICIAN LOS atributos de la clase
    largo = 50
    ancho = 20
    color1 = "Negro"
    color2 = "Azul"
    motores = 4
    activada = False
    compuertaPrincipal = False
    sistemaDefensa = True
    autoDestruccion = False#TERMINAN Los atributos
    Marca = input("Marca: ")# se piede al usuario teclear la marca de la nave

    def encender(self):#Comienzan los metodos
        self.activada = True

    def apagar(self):# SELF devuelve el contenido del objeto en el que se ha definido el cálculo.
        self.activada = False

    def abrirCompuerta(self):
        self.compuertaPrincipal = True
        
    def cerrarCompuerta(self):
        self.compuertaPrincipal = False

    def desactivarDefensas(self):
        self.sistemaDefensa = False

    def activarDefensas(self):
        self.sistemaDefensa = True

    def activarAutoDestruccion(self):
        self.autoDestrucccion = True
        mensaje = "Protocolo de autodestruccion activado."
        print(mensaje)
    def estadoMotores(self):
        if(self.activada):
            return "Motores trabajando al 100%"
        else:
            return "Motores apagados"
    def estadoCompuertas(self):
        if(self.compuertaPrincipal):
            return "La compuerta esta abierta"
        else:
            return "La compuerta esta cerrada"

    def estadoDefensa(self):
        if(self.sistemaDefensa):
            return "El sistema de defensa esta activado"
        else:
            return "peligro!!! El sistema de defensa esta desactivado"#Fin de los metodos

nave1 = Naves()#se crea el primer objeto de nombre nave1 igual a la clase Naves()
#de esta manera nave1 tomara todos los atributos y metodos de la clase Naves ()
nave1.abrirCompuerta()#nave1 abre las compuertas con el metodo abrirCompuerta()
print(nave1.estadoCompuertas())#se imprime el estado de las compuertas mediente el metodo estadoCompuertas()
nave1.cerrarCompuerta()
print(nave1.estadoCompuertas())
nave1.encender()
print(nave1.estadoMotores())
nave1.activarDefensas()
print(nave1.estadoDefensa())
print("Peso de la nave1: ", nave1.peso, "kg")#se imprimir el atributo peso de la clase
print("Marca de la nave: ", nave1.Marca)# se imprime el atributo Marca de la clase
