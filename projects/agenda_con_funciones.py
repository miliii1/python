registro = {}

def agendar_contacto(name, telefono):
    if name in registro:
        print(f"El contacto {name} ya esta registrado.")
    else:
        registro[name] = telefono
        print(f"El contacto {name} ha sido registrado con el número {telefono}.")

    
def search_contacto(name):
    if name in registro:
        print(f"El contacto {name} tiene el número {registro[name]}.")
    else:
        print(f"El contacto {name} no esta registrado.")


def delete_contacto(name):
    if name in registro:
        del registro[name]
        print(f"El contacto {name} ha sido eliminado.")
    else:
        print(f"El contacto {name} no esta registrado.")

    
def listar_contactos():
    if registro:
        print("Lista de contactos: ")
        for name, telefono in registro.items():
            print(f"{name}: {telefono}")
    else:
        print("No hay registro de contactos.")


def main():
    
    while True:
        print("\nAgenda de contactos.")
        print("1. Agendar contactos")
        print("2. Buscar contactos.")
        print("3. Eliminar contactos.")
        print("4. Listar contactos")
        print("5. Salir\n")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            name = input("Ingrese el nombre: ")
            telefono = input("Ingrese número de teléfono: ")
            agendar_contacto(name, telefono)

        elif opcion == "2":
            name = input("Ingrese el nombre: ")
            search_contacto(name)

        elif opcion == "3":
            name = input("Ingrese el nombre: ")
            delete_contacto(name)

        elif opcion == "4":
            listar_contactos()

        elif opcion == "5":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Elige una opción del menú.\n")

    
main()
