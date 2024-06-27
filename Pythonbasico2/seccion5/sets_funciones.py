lenguajes1 = {"Python", "C++","Java"}
lenguajes2 = { "Cobolt", "Java", "C#"}

todos_lenguajes = lenguajes1.union(lenguajes2)
print(todos_lenguajes)

#Clase 2

coincidencias_lenguajes = lenguajes1.intersection(lenguajes2)
print(todos_lenguajes)

#clase 3

print(lenguajes1.isdisjoint(lenguajes2))

mas_lenguajes={"Javascript", "Swift"}
print(lenguajes1.isdisjoint(mas_lenguajes))

#Clase 4

diferencias = lenguajes1.difference(lenguajes2)
print(diferencias)