x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
print(f"Tus número ingresados son: {x} y {y}")

operator = input("Ingrese la operación: ")

if operator == '+':
    print(f"La suma de {x} y {y} es:", x + y)
elif operator == '-':
    print(f"La resta de {x} y {y} es", x - y)
elif operator == '*':
    print(f"La múltiplicacion de {x} y {y} es:", x * y)
elif operator == '/':
    print(f"La división de {x} y {y} es:", x / y)
else:
    print("Operación no disponible")