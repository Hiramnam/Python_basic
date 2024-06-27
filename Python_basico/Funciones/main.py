#Generadores
"""
def pares(): # Generador -> Lazy iterator iteración peresosa 
    for numero in range(0,100, 2):
        yield numero
        
        #return(numero)

        #print('Un mensaje despúes de return')
for par in pares():
    print(par)"""
"""
def pares():
    for numero in range(0, 100, 2):
        yield numero 

        print('Se reanuda la ejecución')
        
generador = pares()

print(next(generador))

print(next(generador))

print(next(generador))

print('Ejecutamos código entre un llamado y otro')

print(next(generador))

print(next(generador))
"""
def pares():
    for numero in range(0, 12, 2):
        yield numero

        print('Se reanuda la ejecución')

generador = pares()

while True:
    try:
        par=next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizó.')
        break