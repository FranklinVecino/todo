#Ejercicio 11: Comparación de tres números con operadores lógicos

#Crea un programa que pida tres números y determine si el primero es mayor que el segundo y si el segundo es mayor que el tercero.

print("dame tres numeros y los comparare")

a = int(input("dame el primer numero: "))
b = int(input("dame el segundo numero: "))
c = int(input("dame el tercer numero: "))

if (a > b and b > c):
    print("el primero es mayor que el segundo y el segundo es mayor que el tercero")
    
else: print("no se cumple la condicion")