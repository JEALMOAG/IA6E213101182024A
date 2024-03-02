"""
Jesus Alejandro Montes Aguila 21310118
20 febrero 2024
Practica 48-50
"""
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 48
'''Diccionario, es muy parecido a una tupla o una lista, con la diferencia de
que se puede buscar dentro del diccionario con el nombre de la variable, ejemplo "diccionario['variable']"'''
teclado2 = {
    'Categoria' : 'Teclados',
    'Modelo' : 'Corsair K55 RGB',
    'Precio' : '59,99$'
    }
print('El modelo ' + teclado2['Modelo'] + 'cuesta ' + teclado2['Precio'])

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 49 invocacion de elemento de diccionario. Si se quiere el elemento de la izquierda se dentro de un diccionaro se{for i in diccionario}pide print(i),
#pero si se quiere el lado derecho print(diccionario[i])
teclado1 = {
    'Categoria' : 'Teclados',
    'Modelo' : 'HyperX Alloy FPS Pro',
    'Precio' : '123,45'
    }
teclado1['Precio'] = '89,99'
for i in teclado1:
    print(i + " = " + teclado1[i])
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Practica 50 se tuliza el metdo del diccionario para borrar todo un diccionario, pero tambien se puede borrar elementos de dicho diccionario del diccionario['elemento']
teclado3 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado4 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
del teclado3
del teclado4['Categoría']
del teclado4['Precio']
print(teclado4['Modelo'])
    

    
