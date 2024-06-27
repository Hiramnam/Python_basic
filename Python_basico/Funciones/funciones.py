"""
def suma(numero_uno, numero_dos):
 
    resultado = numero_uno + numero_dos
  
    print(resultado)

numero_uno = int(input('Ingresa el primer número entero:'))#String
numero_dos = int(input('Ingresa el segundo número entero:'))

suma(numero_uno, numero_dos)"""

"""
def suma(n1,n2):
    resultado = n1 + n2
    print(resultado)

numero_uno = int(input('Ingresa el primer número entero:'))#String
numero_dos = int(input('Ingresa el segundo número entero:'))
suma(numero_uno, numero_dos)
"""
def suma(n1, n2):
    resultado = n1 + n2
    return n1 + n2, 'La función retornar 2 valores'

numero_uno = int(input('Ingresa el primer número entero:'))#String
numero_dos = int(input('Ingresa el segundo número entero:'))

resultado, mensaje = suma(numero_uno, numero_dos)
print('El  resultado es:', resultado)
print(mensaje)
