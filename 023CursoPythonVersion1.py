"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 43
"""
# Capitulo 43 Variables globales, locales,funciones anidadas\
    #las funciones anidadas permite el uso de variables locales de su funcion anidadora pero no biceversa\
        # osea la funcion anidadora no puede usar las variables de la funcion anidada.

num4 = 10 # variable global
def SUMA(): # decalracion de funcion 
    num1 = int(input("Ingresa un numero: "))# variable 1 local
    num2 = int(input("Ingresa otro numero: "))#variable 2 local
    result = num1 + num2 #variable 3 local
    print("Suma: ", result)
    
    def RESTA(): # declaracion de funcion anidada
        print("\nEl siguiente numero que teclearas restara al resultado anterior\n")
        num3 = int(input("\nIngresa un tercer numero: ")) #variable 4 local dentro de una funcion anidada 
        global result2 # se transforma una variable local a global mediante el METODO "Global variable"
        result2 = result - num3 # se hace una resta de una variable local - vaiable local anidada y su resultado se guarda en una variable global
        print("Resta: ",result2)# se imprime un varible global
    RESTA()

SUMA()

print("Multiplicacion = 10 * Resta = ", num4 * result2 ) # mutiplicacion de variable local transformada a global con una varibale meramente global 