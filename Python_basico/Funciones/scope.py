#Scope
animal = 'León' #vaiable global -> función, condicion  o ciclo

def imprimir_animal():
    global animal
    animal = 'Ballena'

    tipo = 'Mamifero'# variable local
    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))



