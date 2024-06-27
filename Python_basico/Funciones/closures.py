"""
e = 'e' #variable global
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c' #Variables locales


        print(a)
        print(b)
        print(id(b))
        print(e)

    funcion_anidada()
    #print(c)

funcion_principal()
"""
"""
def saludar():
    def mostrar_mensaje():
    
        print('Hola, nos encontramos en el curso de Python')
    
    return mostrar_mensaje

respuesta = saludar()
respuesta()
"""
def saludar(username):
    mensaje = f'Hola {username}'#variable local

    def mostrar_mensaje(): #anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)
respuesta()

