registro = {}

usuario = input("Ingrese nombre de usuario: ")

if usuario in registro:
    print("Usuario válido, puedes continuar: ")
    contraseña = input("Ingrese contraseña: ")
    valid_password = ("PYnative@#2023")
    if contraseña == valid_password:
        print("Bienvenido a tu cuenta!. ")
    else:
        print("Usuario inválido. Contacto a su administrador. ")
