"""
Jesus Alejandro Montes Aguila 21310118
02 marzo de 2023
Capitulos 45 y 46
    %d dia del mes / 01-31
    %a dia de la semana / mi,ma,etc
    %A dia de la semana / miercoles,martes,etc
    %w dia de la semana / 0-6
    %b mes corto/mar
    %B mes entero/ marzo 
    %m numero de mes/01-12
    %y año corto/20 o 24 
    %Y año largo/ 2020 o 2024
    %H hora/00-23
    %I Hora/00-12
    %p AM-PM
    %M minutos / 00-59
    %s segundos / 00-59
    %f microsegundos / 000000-999999
    %j dia del año/ 001-366
    %U numero de la semana del año D/ 00-53
    %W numero de la semana del año L/00-53
    %Z Zona horario/ UTC
    %c Fecha y hora local/ 03/03/2024 10:15:45
    %x fecha local / 03/03/2024
    %X hora loca / 10:15:45
    """
#Capitulo 45 y 46 fechas y horas\ 
# para saber la hora exacta y en un fromato de dia, mes, año, hora, minutos y segundo\
    #es necesario importar una libreri llamada datetime, en caso de que desees hacer una \
        # traduccion deberas importar la libreria locale, puesto que la librerio datetime esta ingles.
import datetime,locale # se importan las librerias 
locale.setlocale(locale.LC_ALL, "es-ES") # se hace la traduccion de ingles a español
fecha = datetime.datetime(2003,6,23) # se define una fecha año/mes/dia
fecha1 = datetime.datetime.now()# se crea un objeto el contine la fecha exacta actual
fecha2 = datetime.datetime(2017,3,17,9,45,23)# se define un fecha año/mes/dia/hora,minuto,microsengundo
print(fecha)
print(fecha1)
print(fecha2)
print("Año:",fecha1.year)# se impre el año actual 
print("Mes:",fecha1.month)# se imprime el mes actual
print("Day:",fecha1.day)# se imprime el dia actual 
print("Hora:",fecha1.hour)# se imprime la hora actual 
print("Minuto:",fecha1.minute) # se imprime el minuto actual 
print("Segundo:",(fecha1.microsecond)) # se imprime el microsengudo atual
print(fecha1.strftime("%A"))# se imprime mediante el metodo strftime (strin format time) el dia de la semana actual
print(fecha.strftime("%A"))# se imprime mediante el metodo strftime el dia en que naci