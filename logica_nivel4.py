# 1. Verificar si dos listas son iguales (sin usar ==)
# Escribí una función que reciba dos listas y devuelva True si tienen los mismos elementos en el mismo orden, y False si no.

def listasIguales(lista1, lista2):
    if len(lista1) != len(lista2):
        return False
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            return False
    return True

print(listasIguales([1, 2, 3], [3, 2, 1]))
print(listasIguales([1, 2, 3], [1, 2, 3]))

# 2. 2. Invertir una lista (sin usar [::-1] ni reverse())
# Crea una función que reciba una lista y devuelva una nueva lista con los elementos en orden inverso.

def listaInversa(lista):
    newList = []
    for i in lista:
        newList.insert(0, i)
    return newList

print(listaInversa([1, 2, 3]))

# 3. Crear un diccionario con conteo de elementos
# Dada una lista, devolvé un diccionario que indique cuántas veces aparece cada elemento.
def contarElementos(lista):
    count = {}

    for i in lista:
        count[i] = count.get(i, 0) + 1

    return count

print(contarElementos([1, 2, 1, 3, 2, 1]))

# 4. Saber si una palabra es un anagrama. Dos palabras son anagramas si tienen las mismas letras pero en diferente orden.
"""(Tip: podés ordenar ambas palabras y comparar)."""

def wordIguales(text1, text2):
    return sorted(text1) == sorted(text2)

print(wordIguales("amor", "roma"))
print(wordIguales("hola", "olah"))
print(wordIguales("perro", "gato"))

# 5. Simular un login
"""Pedile al usuario un nombre y contraseña. Si ambos coinciden con los valores almacenados (por ejemplo "admin" y "1234"), mostrale "Bienvenido".
Caso contrario, 'Acceso denegado'."""

user = input("Enter your user: ")
password = input("Enter your password: ")

if user == "admin1" and password == "1234":
    print("Bienvenido." )
else:
    print("Acceso denegado.")


# 6. Extraer solo los números pares de una lista. Crear una función que reciba una lista de enteros y devuelva solo los pares.}

def numPares(num):
    return [x for x in num if x % 2 == 0]

print(numPares([1, 2, 3, 4, 5, 6, 7, 8]))

#7. Buscar la palabra más larga. Crear una función que reciba una lista de palabras y devuelva la más larga.

def wordLarge(lista):
    return max(lista, key=len)

print(wordLarge(["gato", "perro", "elefante"]))
