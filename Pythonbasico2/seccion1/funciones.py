lista =[1,3]
lista.append(4)
#print(lista)
lista.extend([5,6,7])
#print(lista)
lista.insert(1,2)#(indice, valor)
#print(lista)

letras=["x", "Y", "Z"]
letras.remove("Y")
#print(letras)

numeros = [1,2,2,2,2,2,3,4,5] #elimina el numero seleccionado, si está repetido se eliminará una vez
numeros.remove(2)
#print(numeros)

nombres = ["Juan", "Elena", "Pedro", "Maria"]
nombres.pop()# Se eliminará el último elemento
#print(nombres)

nombres.pop(1) #El inidce del elemento que se quiere borrar
#print(nombres)

print(numeros.count(2))

numeros = [1,2,2,2,2,3,4,5]
#print(numeros.count(2))

mas_letras = ["a", "b","c", "d","d"]
#print(mas_letras.index("b"))
#print(mas_letras.index("d"))
print(len(mas_letras))
