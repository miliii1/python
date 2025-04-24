# EJERCICIO 1 – Herencia básica
"""
Creá una clase Persona con nombre y edad, y un método saludar() que imprima algo como: "Hola, soy [nombre] y tengo [edad] años."
Luego, creá una subclase Estudiante que herede de Persona y agregue el atributo carrera y el método estudiar() que diga: "Estoy estudiando [carrera].
"""
"""
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludar(self):
        print(f"Hola, soy {self.name} y tengo {self.age} años.")


class Student(Person):

    def __init__(self, name, age, carrer):
        super().__init__(name, age)
        self.carrer = carrer


    def carrera(self):
        print(f"Estoy estudiando: {self.carrer}")


myStudent = Student("Nova", 22, "Ingeniería en Sistemas")
myStudent.saludar()
myStudent.carrera()
"""
# EJERCICIO 2 – Herencia con comportamiento propio
"""
Usá tu clase Auto de antes (con marca y modelo) y creá una subclase AutoDeportivo que agregue un atributo turbo (booleano) 
y el método activar_turbo(), que imprima un mensaje especial si tiene turbo.
Extra: agregale un método __str__() para que cuando lo imprimas diga, por ejemplo:
"Lamborghini Huracan - Turbo: Sí
"""
class Auto:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False


    def arrancar(self):
        self.enmarcha = True
        print(f"El {self.marca} {self.modelo} está en marcha.")


class AutoDeportivo(Auto):

     def __init__(self, marca, modelo, turbo):
        super().__init__(marca, modelo)
        self.turbo = turbo
    
     def tiene_turbo(self):
        if self.turbo:
            print(f"El auto: {self.marca} {self.modelo} SI tiene turbo")
        else:
            print(f"El auto: {self.marca} {self.modelo} NO tiene turbo")
            
     def __str__(self):
        status_turbo = "Sí" if self.turbo else "No"
        return f"{self.marca} {self.modelo} - Turbo: {status_turbo}"
  


miCoche = AutoDeportivo("Fiat", "FastBack", False)
miCoche.tiene_turbo()
print(miCoche)

miCoche2 = AutoDeportivo("Lamborgini", "BWW", True)
miCoche2.tiene_turbo()
print(miCoche2)
