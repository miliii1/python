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

# 3. Adivina el número
"""
Escribir un pequeño juego donde el programa genera un número del 1 al 10, y el usuario debe adivinarlo. El programa da pistas si es mayor o menor.
(Pista: usá import random y random.randint(1, 10))

"""

import random

numSecret = random.randint(1, 10)
intentos = 0

while intentos < 3:

    try:
        num = int(input("Enter your number: "))
    except ValueError:
        print("No es un número valido.")
        continue
    
    if num == numSecret:
       print("Felicidades! adivinaste el numero!.")
       break

    elif num > numSecret:
        print("El numero debe ser más chico.")
    else: 
        print("El numero debe ser más grande.")

    intentos += 1
    print(f"Te quedan {intentos} intentos. ")

if intentos == 3:
    print(f"Se acabaron los intentos el numero era: {numSecret}")

# EJERCICIO 4: Generador de contraseñas:
"""
Que arme una contraseña aleatoria usando letras, números y símbolos.
(Usás import random y string)
"""
import random
import string
import secrets

caracteres = string.ascii_letters + string.digits + string.punctuation

passLongitud = 8
password = []

password.append(random.choice(string.ascii_letters))
password.append(random.choice(string.digits))
password.append(random.choice(string.punctuation))

while len(password) < passLongitud:
    password.append(secrets.choice(caracteres))

random.shuffle(password)

password = "".join(password)

print (f"Tu contraseña es: {password}")


# EJERCICIO 5: Contador de palabras en un texto:
"""
Recibís un string largo y devolvés cuántas palabras tiene.
(Pista: texto.split())

"""
texto = input("Ingrese un texto: ")

newText = texto.split()

print(len(newText))

# 6. Suma de dígitos:

"""Dado un número, devolvé la suma de sus dígitos.
(Ej: 123 ➔ 6 porque 1+2+3=6)"""

def sumar_digitos(num):
    numero = [int(x) for x in str(num)]
    suma = sum(numero)
    return suma

print(sumar_digitos(123))


#7. Invertir una lista:

"""Recibís una lista y la devolvés al revés.
(Ej: [1,2,3] ➔ [3,2,1])"""

def list_reverse(lista):
    return lista[::-1]

print(list_reverse([1, 2, 3]))

#8. Sacar elementos impares:

"""Recibís una lista y devolvés solo los pares.
(Ej: [1,2,3,4,5] ➔ [2,4])"""

def num_pares(lista):
    lista_par = []
    lista_impar = []
    for i in lista:
        if i % 2 == 0:
            lista_par += [i]
        else:
            lista_impar += [i]
            
    return lista_par
    #return lista_impar
        
print(num_pares([1, 2, 3, 4, 5]))


# =============== NIVEL 4: =============
# 1. Calcular el factorial de un número. (Ej: 5 ➔ 5 × 4 × 3 × 2 × 1 = 120) (Pista: usá un bucle for.)

def num_factorial(num):
    if num > 0:
        return num * num_factorial(num - 1)
    else:
        return 1
    
print(num_factorial(5))

#2. Encontrar el máximo de una lista sin usar max(). (Ej: [5, 7, 2, 9, 1] ➔ 9)

def max_lista(lista):
    lista_max = sorted(lista, reverse=True)
    return lista_max[0]

print(max_lista([5, 7, 2, 9, 1]))



def contarLista(lista):
    return len(lista)
    
    
print(contarLista([10, 20, 30]))

# 3. Contar elementos de una lista

""" 
Crear una función que reciba una lista y devuelva cuántos elementos contiene.
(Usá len() adentro de la función).
[10, 20, 30] ➔ 3 elementos """


---

# 4. Eliminar duplicados sin set()

"""Crear una función que elimine los elementos duplicados de una lista, sin usar set().
Tendrás que armar una nueva lista y agregar solo los elementos que todavía no estén."""
# [1, 2, 2, 3, 4, 1, 5] ➔ [1, 2, 3, 4, 5]



---

#5. Comprobar si un número es palíndromo

"""Crear una función que reciba un número y diga si es palíndromo (es igual al revés).
(Tip: convertí el número en string).
121 ➔ Palíndromo ✅
123 ➔ No es palíndromo ❌
"""

---

# 6. Suma de valores únicos en una lista

"""Crear una función que sume solo los valores que aparecen una sola vez en una lista.
[1, 2, 3, 2, 1] ➔ 3
(porque el 3 es el único que aparece una sola vez)"""


---

#7. Contar vocales en un string

"""Crear una función que reciba un texto y devuelva cuántas vocales tiene.
(Tip: podés recorrer el texto con un for y contar las vocales).
"Hola Mundo" ➔ 4 vocales """
