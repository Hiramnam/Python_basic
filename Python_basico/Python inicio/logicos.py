#and, or y not
# ayuda a implementar booleanos
#and
resultado_final = True and True

print(resultado_final)

resultado_final = False and False
print(resultado_final)

resultado_final = True and True and 10 > 20

print(resultado_final)


resultado_final = True and True and 10 < 20

print(resultado_final)

# or
resultado_final = True or True or 10 > 20

print(resultado_final)

resultado_final = False or False
print(resultado_final)

resultado_final = False and (False or 5 > 10) # primero va resolver lo que está entre parentesis

print(resultado_final)

#not
resultado_final =  not False #niega el comendo puesto en este caso se niega el false
#niega el valor booleano
print(resultado_final)