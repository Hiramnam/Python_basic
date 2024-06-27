nombre = 'Carlos Hiram '
apellido = 'Navarro'

#nombre_completo = 'Ing. ' + nombre + '' + apellido + '.'

#nombre_completo = 'Mr. %s %s %s .' %(nombre, apellido, 'Moreno')

#nombre_completo = 'Ing. {} {} {}.'.format(nombre, apellido, 'Moreno')
"""
nombre_completo = 'Ing. {nombre} {primer_apellido} {segundo_apellido}.'.format(
nombre = nombre,
primer_apellido = apellido,
segundo_apellido = 'Moreno'
)
""" # se tiene que poner la f antes para avisar que es un fstring
#nombre_completo = f'ing. {nombre} {apellido} {"Moreno"} {True}'



print(nombre, apellido, 'Moreno', (12, 34, 55), sep='-')


