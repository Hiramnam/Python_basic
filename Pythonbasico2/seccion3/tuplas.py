#Las tuplas son inmutables, osea no pueden ser modificables
tupla =("a","b","c")

tupla2 = 1,2,3,4

tupla_combinada =("a",2,"c",4.4)

print(tupla_combinada)
print(tupla_combinada[0])

tupla_grande=("Python","Java","C++","Javascript","Cobol","Basic")
print(tupla_grande[2:5])

#clase 2 tuplas
#tupla_combinada[0]= 6
#Generara error porque no puede ser alterada

#aclase 3

tupla_original = ("I","<3", "Codigo", "Facilito")
nueva_lista = list(tupla_original)
print(nueva_lista)

lista_original = ["Yo", "<3","Python"]
nueva_tupla = tuple(lista_original)
print(nueva_tupla)

#clase 4 tupla

tupla_letras=("x", "y","z")
for letra in tupla_letras:
    print(letra)