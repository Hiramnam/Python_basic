#Sumatoria de una lista
lista = [2, 4, 6,1, 2]

sumatoria =  0

for num in lista:
    sumatoria += num
print((sumatoria))

#Promedio de una lsita

promedio = 0
for num in lista:
    promedio += num

promedio /= len(lista)
print(promedio)

max = 0
for num in lista:
    if max < num:
        max = num

print(max)

lista_negativa = [-1, -3,-7,-2]

max = lista_negativa[0]
for num in lista_negativa:
    if max < num:
        max = num
print(f'El numero maximo de la lista es: {max}')


min = lista_negativa[0]
for num in lista_negativa:
    if min > num:
        min = num
print(min)