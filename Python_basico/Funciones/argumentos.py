"""
def promedio(listado): #se pone un asterisco para que se aplique la función sin necesidad de después poner corchete

    return sum(listado) / len(listado)

resultado = promedio([10,10,5,7,10])
print(resultado)
""" 
"""
def promedio(*listado)
    print(listado)
    print(type(listado))

    return sum(listado) / len(listado)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)
"""
"""
def promedio(*args): # cuando se pone asterico se recomienda usar args como argumento

    print(args)
    print(type(args))

    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)"""
#El uso de asterisco no nos limita a usar otros parametros
"""
def promedio(*args):
    return sum(args) / len(args)

def combinacion(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

combinacion(10, 20, 1)

def promedio(*args):
    return sum(args) / len(args)

def combinacion(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

combinacion(10, 20, 1)

"""
"""
def promedio(*args):
    return sum(args) / len(args)

def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2,3,4,5,6,7,8, p4= 1000)
"""
def promedio(*args): #tupla
    return sum(args) / len(args)

def usuarios(**kwargs): # Dict diccionario
    print(kwargs)
    print(type(kwargs))

    usuarios(Hiram = [10,10,9], Juan = [ 10, 7, 9])

    def combinacion(*args, **kwargs):
        print(args)
        print(kwargs)

        combinacion(1,2,3,4,5, cody=True, curso='Python')
        print(combinacion)