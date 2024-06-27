directorio_direcciones ={
    "Elena": "Roma 123, Italia",
    "Juana": "Paris 22A, Francia",
    "Pablo": "Malaga 89, España"
}

print(directorio_direcciones["Juana"])
print(directorio_direcciones.get("Pedro", "Persona no encontrada en el directorio"))

direccion_buscar = "Blvd 1, México"

if(direccion_buscar in directorio_direcciones.values()):
    for persona, direccion in directorio_direcciones.items():
        if(direccion_buscar == direccion):
            print(persona)
else:
    print("No existe la direccion indicada")