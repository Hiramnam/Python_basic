diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

print('a' in diccionario)
"""
valor = diccionario['d']
print(valor)
"""
#get
#setdefault
#valor = diccionario.get('a', ' La llave no existe en el dict.')
valor = diccionario.setdefault('e', 5)
print(valor)

