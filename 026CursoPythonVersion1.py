"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 47,48,49 y 50
"""
#Capitulo 47 expresiones reguales 
#findall(), search(), split(), sub()
import re #regular expresions 

texto = "Bienvenidos a CETI"
busquedad = re.search("Bienvenidos a",texto)
print(busquedad)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Capitulo 48 expresiones reguales 
#findall(), search(), split(), sub()  
mensaje = "El término Google existe desde 1938 \
            y fue gracias a que el matemático, Edward\
               Kasnerle pidió a su sobrino de tan sólo \
                   9 años que inventara un nombre para un \
                       número muy grande."
busquedad1 = re.findall("un",mensaje)
print(busquedad1)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Capitulo 49 expresiones reguales 
#findall(), search(), split(), sub()
comunicado = "Hace tiempo que la inteligencia artificial \
                abandonó el espectro de la ciencia ficción para\
                    colarse en nuestras vidas y, aunque todavía\
                        en una fase muy inicial, está llamada a\
                            protagonizar una revolución equiparable\
                                a la que generó Internet. "

resultado = re.split("la",comunicado)
print(resultado)
resultado = re.sub("en", "###",comunicado)
print(resultado)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Capitulo 50 expresiones reguales 
#Secuencias especiales 
#\A,\b,\B,\d,\D,\s,\S,\w,\W,\Z
#METACARACTERES [],\,.,*,$,+,(),{},|,^
speech = "Hola soy jesus y estudio semestre 6 Ing. Mecatronica en CETI  y  semestre 1 Ing. Comunicacion y Electronica en CUCEI"

result = re.findall("\AHola soy",speech)# \A solo encuentra los primeros caractes de la cadena, si y solo si esta contemplado el primer caracter.
print(result)
result1 = re.findall("\D",speech)# \D separa la cadena por comas en cada caracter y omite todos los caracteres numericos
print(result1)
result2 = re.findall("estu...",speech)# busca una palabra a base de una idea y la complemenas con puntos 
print(result2)
result3 = re.findall("CETI|CUCEI|ITESM",speech)# busca cualquier resultado separando con una barra vertical, SIN IMPORTAR SI SE ENCUENTRA O NO. SOLO MOSTRARA LO QUE ENCUENTRE.
print(result3)