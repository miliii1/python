print("Ingresar usuario a la web")
count = 0

while count < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username== "admi1" and password== "1234":
        print("Access valid!")
        break
    else:
        print("Invalid Access. Try again")
        count += 1
        
        
if count == 3:
    print("Se ha pasado el limite de intentos. ")