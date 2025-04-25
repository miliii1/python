# NIVEL 1: 
# # #
# EJERCICIO 1: Dado un número, devolver el doble

#num = int(input("Ingrese un número: "))
#print(num * 2)

# EJERCICIO 2: Dada una lista de números, devolver la suma total.

#num = [1, 2, 3, 4, 5]
#print(sum(num))
"""
numb = input("Ingrese una lista de números: ")
listaDeCadenas = numb.split()

listaDeNum = []

for cadena in listaDeCadenas:
    listaDeNum.append(int(cadena))

suma = sum(listaDeNum)
#print(f"La suma es: {suma}")"""


# EJERCICIO 3: Contar cuántas veces aparece un elemento en una lista.

def contar_list(list, element):
    count = 0
    for i in list:
        if i == element:
            count += 1
    return count

# print(contar_list(["Manzana", 1, 2, 3, 1, "Manzana"], 1))

# EJERCICIO 4: Devolver la cantidad de vocales en un string

def string_vocal(str):
    vocales = ["a", "e", "i", "o", "u"]
    cant = 0
    for i in str:
        if i.lower() in vocales:
            cant += 1
    return cant
        
# print(string_vocal("Hola"))


# ============ Nivel 2 – Más lógica: ============

# EJERCICIO 1: Dado un diccionario de productos (nombre: precio), devolver el más caro.

productos = {
    "Pan": 1200,
    "Leche": 1400,
    "Aceite": 1700,
    "Agua": 1000,
    "Huevo": 1200
}

productoMasCaro = max(productos, key=productos.get) # usamos max con key para obtener el producto de mayor precio
#print(f"El producto más caro: {productoMasCaro}")


# EJERCICIO 2: A partir de una lista de palabras, devolver solo las que empiezan con vocal.

def listaDePalabras(lista):
    vocales = "aeiouAEIOU"
    return [elemento for elemento in lista if elemento.startswith(vocales)]

listaNueva = ["Hola", "Oso", "casa", "ala", "Espada"]
listaConVocal = listaDePalabras(listaNueva)
#print(listaConVocal)

# EJERCICIO 3: Crear una función que reciba un string y devuelva si es palíndromo.

def palindromo(texto):
    textoInvertido = texto[::-1]

    return "Si es palindromo" if texto == textoInvertido else "No es palindromo"

print(palindromo("ala"))
print(palindromo("hola"))


# EJERCICIO 4: Dado un número, devolver True si es primo, False si no.

"""num = int(input("Enter your number: "))
for i in num:
    if num % i == 0:
        print("Es primo")
    else:
        print("No es primo")"""
# me quede estancada nosé que pasa :( jajaja)



# =============== NIVEL 3: LÓGICA Y COMPRENSIÓN =============


# EJERCICIO 1: Eliminar duplicados.

def removeList(lista):
    return set(lista)
    
    
print(removeList([1, 2, 3, 4, 4, 4, 5, 6, 6, 7])) # [1, 2, 3, 4, 5, 6, 7]
print(removeList([1, 2, 2, 3, 4, 1, 5])) # [1, 2, 3, 4, 5]

# EJERCICIO 2: Contar palabras
"""
Pedirle al usuario e imprimir cuantas palabras tiene.
"""

palabra = input("Enter your frase: ")

newPalabra = palabra.split()
print(len(newPalabra))



