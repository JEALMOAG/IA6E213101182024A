"""
Jesus Alejandro Montes Aguila 21310118
03 marzo de 2023
Capitulos 51
"""
#CAPITULO 51 manejo de exepciones 
# try: except: else: finally:
variable = "Correcto."
try: #permite probar un bloque de código en busca de errores. 
    print(variable)
except: #bloque le permite manejar el error.
    print("Hay un error")

restart = True

while restart:
    try:
        num1 = int(input("Introduce un numero para multiplicar: "))
        num2 = int(input("Introduce otro numero para multiplicar: "))
    except ValueError: #exepcion integrada
        print("No has introducido un numero. Vuelve a intentarlo")
    else:#bloque te permite ejecutar código cuando no hay ningún error.
        print("El resultado es: ", num1 * num2)
    finally:#bloque le permite ejecutar código, independientemente del resultado de los bloques try y except.
        pregunta = input("¿Quieres seguir multiplicando? Introduce S/N:\n")
    if pregunta == "N":
        restart = False
    else:
        print("De acuerdo, vamos a seguir multiplicando.")