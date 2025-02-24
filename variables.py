# Variables in Python
"""first_name = 'Nova'
last_name = 'Dainn'
country = 'Argentina'
city = 'Mendoza'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Nova',
   'lastname':'Dainn',
   'country':'Argentina',
   'city':'Mendoza'
   }"""

# Declaring Multiple Variable in a Line
# Multiple variables can also be declared in one line:
"""
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)"""

# Converting str() to list()

"""
first_name = "Novadainn"
print(first_name)
name_to_list = list(first_name)
print(name_to_list)
"""

num = input("Coloca un numero: ")
print(num)

if int(num) > 10:
   print("Numero grande")
  
elif int(num) < 10:
   print("Es menor")
   
else:
   print("NOT")