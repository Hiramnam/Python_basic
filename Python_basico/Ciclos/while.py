#Programa 1
"""
contador = 1

while contador <= 10:
    print(contador)
    
    contador = contador +1
"""
#Programa 2
numero = 123456789
contador_digitos= 0

while numero >= 1:
    #contador_digitos = contador_digitos+1
#la linea de arriba es igual a la de abajo solo que resumido
    contador_digitos += 1
    numero = numero / 10
else: 
    print('Fin del ciclo While')
print(contador_digitos)