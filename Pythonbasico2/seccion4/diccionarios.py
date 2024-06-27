#Clase 1
estudiante={
    "nombre":"Juana",
    "apellido":"De Arco",
    "edad":19,
    "ciudad": "Paris"
}

print(estudiante["nombre"])

estudiante["edad"]=18
print(estudiante)

estudiante["cursos"]=["Python","C++","Java"]
print(estudiante)

#clase 2
for llave in estudiante:
    print(llave)
for llave in estudiante:
    print(estudiante[llave])