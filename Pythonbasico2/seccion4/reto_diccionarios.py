lista_alumnos =[
    {"nombre": "Elena", "apellido": "De Troya", "id":123, "cursos":["Fundamentos de la web", "Python"]},
    {"nombre": "Juana", "Apellido": "De Arco", "id":"234", "cursos":["Fundamentos de la web", "Python", "Mern"]},
    {"nombre": "Pedro", "Apellido": "Páramo", "id":345, "cursos": ["Fundamentos de la web", "Python","Mern","Java"]}
]
lista_alumnos[2]["cursos"].pop(2)
from pprint import pprint
pprint(lista_alumnos)
