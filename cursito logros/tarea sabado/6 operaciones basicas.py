#Ejercicio 6: Operaciones aritméticas básicas

#Desarrolla un programa que pida dos números y realice las cuatro operaciones aritméticas básicas 
# con ellos: suma, resta, multiplicación y división. 
# Debe mostrar los resultados de cada operación.

a = float(input("introduce el primer numero"))
b = float(input("introduce el segundo numero"))

suma = a + b
print(f"si los sumamos nos queda: ",suma)

resta = a - b
print(f"si los restamos nos queda: ",resta)

multiplicacion = a * b
print(f"si los multiplicamos nos queda: ",multiplicacion)

division = a/b
print(f"si los dividimos nos queda: ",division)