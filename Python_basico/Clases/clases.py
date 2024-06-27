#CamelCase
"""
class Usuario: 
    pass 

cody = Usuario()
print(cody)
"""
#Attrs = atributos
#Attrs de clase
#Attrs de instancia
"""
class Usuario:
    username = 'Username por default'
    email = ''
Usuario.username = 'User1'
Usuario.email = 'inf@codigofacilito.com'

print(Usuario.username)
print(Usuario.email)
"""
"""
class Usuario:
    #Attrs de clase
    username = 'Username por default'
    email = ''
    #__dict__
user1 = Usuario()
#1. verifica si el attr existe dentro del objeto
#2. verifica si el attrs existe dentro de la clase -> solo servirá para lectura
#3. lanzar un error
user1.username='Cody'#añadimos un atributo al objero
user1.password = '1234'
print(user1.username) #de isntancia

print(id(user1.username))
print(id(user1.username))

user1.password = 'password'
print(user1.__dict__) #Dict
"""
#Métodos
"""
class Usuario:
    #__init__
    def inicializar(self, username, password):
        #añadiendo attrs al objeto
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

user1.inicializar('user1','password1')
user2.inicializar('user2','password2')
user3.inicializar('Cody', 'password3')
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
"""
#INIT

#Object
class Usuario:

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

user1 = Usuario('user1','password1')
user2 = Usuario('user2','password2')
user3 = Usuario('user3', 'password3')

user4 = Usuario()

print(user1.__dict__)#atriburo que es un dict diccionario
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)