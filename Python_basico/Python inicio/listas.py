lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']
lista_cursos_2=['C', 'C++', 'Docker']
"""
primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

ultimo_curso = lista_cursos[4]
print(ultimo_curso)

#para actualizar o modificar los listados
#se utiliza

#lista_cursos[2] = 'Rust'
print(lista_cursos) 
#con este se modificará el numero dos en este caso Flask fue removido

#Sublistas
sub_lista = lista_cursos[0:3]
print(sub_lista)
#[start:end]  no se tomaria el indice final
sub_lista = lista_cursos[1:4]
print(sub_lista)

sub_lista = lista_cursos[1:]# indica que quieres obtener todos los indices de la lista apartir del inicial

print(sub_lista)

#[start:end]
#[start:] -> obtenemos los últimos elementos de la lista
sub_lista = lista_cursos[4:]
print(sub_lista)
sub_lista = lista_cursos[:4]
print(sub_lista)

sub_lista = lista_cursos[1:5:2] #con esto dará saltos de dos en dos
print(sub_lista)

sub_lista = lista_cursos[::2] #da saltos de dos en dos

print(sub_lista)

sub_lista = lista_cursos[::-1] #modifica el orden de la lista a la inversa
print(sub_lista)


#Añadir elementos a la lista
print(len(lista_cursos))
lista_cursos.append('MongoDB')
lista_cursos.append('c#')
lista_cursos.append('JavaScript')

lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'PyGame')

lista_cursos.extend(lista_cursos_2)
 #añade todos los elementos de la segunda lista a la primera sin afectar a la segunda


print(lista_cursos)
print(len(lista_cursos))
print(lista_cursos_2)

#elminar elementos de la lista
lista_cursos.remove('MongoDB')
del lista_cursos[0]
lista_cursos.clear () #borra todos los elementos de la lista
print(lista_cursos)
"""



