#DESAFÍO 5.1 – Promediar calificaciones
#Dada una lista de diccionarios donde cada diccionario representa a un alumno con su nombre y lista de calificaciones, devolvé otro diccionario con los nombres y sus promedios.
# Pista: vas a tener que recorrer cada alumno con un for, extraer las notas, sacar el promedio y armar el nuevo diccionario.

def promedioAlumnos(alumnos):
    promedios = {}

    for i in alumnos:
        name = i["nombre"]
        note = i["notas"]
        promedio = sum(note) / len(note)
        promedios[name] = promedio

    return promedios




alumnos = [
    {"nombre": "Ana", "notas": [7, 8, 9]},
    {"nombre": "Luis", "notas": [6, 5, 7]},
    {"nombre": "Sofía", "notas": [10, 9, 10]}
]

print(promedioAlumnos(alumnos))