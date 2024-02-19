"""
Jesus Alejandro Montes Aguila 21310118
19 febrero 2024
Practica 42-
"""
print("menu".title())
while True:
    opc = input("\n\ta)P42.\n\tb)P43.\n\tc)P44.\n\td)P45.\n\te)P46.\n\tf)P47\n\tg)Salir\n\t").lower()
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #practica 42
    if(opc=='g'):
        break
    if(opc=='a'):
        x = 0
        while x < 15:
            x += 5
            print(x)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #practica 43
    if(opc=='b'):
        y = 0
        while y > -100:
            y-=20
            print(y)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #practica 44
    if(opc=='c'):       
        z = 10
        while z >= 0:
            print('El valor del bucle es: ',z)
            z-=1
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #practica 45
    if(opc=='d'): # loop while e if andeas del con medofo continue el cual omite o hace salto en ciertas iteraciones
        x1 = 0
        while x1 <= 30:
            x1 += 1
            if x1==4 or x1==6 or x1==10:
                print('\tSe salto el valor',x1,'de x')
                continue
            if x1 == 15:
                print('Se rompio la ejecucion del bucle cuando x valia: ',x1)
                break
            print('El valor del bucle2 es: ', x1)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #practica 46
    if(opc=='e'):#ciclo FOR for x in variable,lista, etc
        colores = ('rojo','azul','verde','amarillo')
        for color in colores:
            print('El color es: ', color,"." )
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    #practica 47
    if(opc=='f'): # loop for con rango for i in range(numero inical, numero final, intervalo)
        for i in range(7,700,100):
            print(i)
