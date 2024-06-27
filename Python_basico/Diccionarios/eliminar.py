diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

del diccionario['a']
valor = diccionario.pop('b')

print(valor)

diccionario.clear()
print(valor)

print(diccionario)
print(len(diccionario))
