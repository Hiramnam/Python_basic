"""
lenguajes = 'Python-Ruby-Java-Rust-C++-C'

#split va a generar y retornar un nuevo listado

listado_lenguajes = lenguajes.split('-')
#En el split se pone un caracter que quieras usar de espaciador
#entre los parentesis y te dara como resultado el mismo resultado de espaciamiento
#que sería ", y espacio"
print(listado_lenguajes)
"""
lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
string_lenguajes =' '.join(lenguajes)
string_lenguajes ='/'.join(lenguajes)
print(string_lenguajes)
#con el metodo join podemos unir cada uno de los elementos del listado
#mediante un caracter o grupo de caracteres
