"""
#Herencia
class Mascota: #Clase Padre
    
    def comer(self):
        print('La mascota come.')

    def formir(self):
        print('La mascota duerme.')

class Perro(Mascota): #Clase hija
    pass

class Gato(Mascota):
    pass
duke = Perro()

duke.comer()
duke.dormir()
patricio = Gato()
patricio.comer()
patricio.dormir()
"""


#Herencia multiple
"""
class Mascota:

    def comer(self):
        print('La mascota come.')

    def dormir(self):
        print('La mascota duerme.')
class Felino:
    def cazar(self):
        print('El felino caza.')

class Gato(Mascota, Felino):
    pass
patricio = Gato()

patricio.comer()
patricio.dormir()

patricio.cazar()
    """
#Sobre escritura
"""
class SerVivo:
    def dormir(self):
        print("El ser duerme.")

class Animal(SerVivo): #Clase Padre
    def comer(self):
        print('El animal come.')

    #def dormir(self):
       # print('El animal duerme.')

class Mascota(Animal): #Clase padre 
    def comer(self):
        print('La mascota come.')

class Felino: 
    def cazar(self):
        print('El felino caza.')

class Gato(Mascota, Felino):
    
    def __init__(self,nombre):
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre} come.')
    
    #def dormir(self):
       # print(f'{self.nombre} duerme.')

patricio = Gato('Patricio')
patricio.comer()
patricio.dormir()
""" 
#Sobre escritura 2
class SerVivo:
    def dormir(self):
        print("El ser duerme.")

class Animal(SerVivo): #Clase Padre
    def comer(self):
        print('El animal come.')

    #def dormir(self):
       # print('El animal duerme.')

class Mascota(Animal): #Clase padre 
    def comer(self):
        super().comer()
        print('La mascota come.')

class Felino: 
    def cazar(self):
        print('El felino caza.')

class Gato(Mascota, Felino):
    
    def __init__(self,nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'{self.nombre} come.')
    
    #def dormir(self):
       # print(f'{self.nombre} duerme.')

patricio = Gato('Patricio')
patricio.comer()
patricio.dormir()