carreras: tuple[str, ...] = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas: list[tuple[str, str, int, int]] = [

]

estudiantes: list[dict[str, str | int]] = [

]


for _ in range(5):
    print(f"\nIngresando datos del estudiante:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad (entero): "))
    carrera = int(input("Carrera (0, 1 o 2): "))
    
    nueva_persona = (nombre, apellido, edad, carrera)
    personas.append(nueva_persona)
    print("")

for p in personas:
    nombre, apellido, edad, indice_carrera = p
    
    nombre_carrera = carreras[indice_carrera]
    
    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": nombre_carrera
    }
    
    estudiantes.append(estudiante)

for e in estudiantes:
    print(f"{e['nombre']} {e['apellido']} tiene {e['edad']} años y estudia {e['carrera']}")