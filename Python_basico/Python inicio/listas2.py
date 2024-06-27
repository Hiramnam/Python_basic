lista = [8, 90, 1 , 5, 44, 132, 600, 3, 4]

lista.sort(reverse=True)

#print(lista[0]) #min
#print(lista[-1])#max
#print(min(lista))
#print(max(lista))

#para buscar un elemento y saber si está en 
#el listado

#print(10 in lista) da false porque no está en lista
#print(5 in lista) da true si está en lista
#print(11 not in lista) #da true porque 11 no está en lista
#print(8 not in lista) da falso porque si está en lista

print( 5 in lista)
index = lista.index(5)
print(index)