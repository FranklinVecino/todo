#Ejercicio 8: Información del usuario

#Crea un programa que pida al usuario su nombre, edad y ciudad de residencia. 
#Al final, debe mostrar un mensaje con toda la información ingresada, por ejemplo: "Nombre: [nombre], Edad: [edad], Ciudad: [ciudad]".

print("\ndame tus datos")

nombre = str(input("ingresa tu nombre: "))
edad = int(input("ingresa tu edad: "))
ciudad = str(input("ingresa el nombre de tu ciudad de residencia: "))

print("\nestos son los datos proporcionados: ")
print(f"nombre:", nombre)
print(f"edad:", edad)
print(f"ciudad de residencia:", ciudad)