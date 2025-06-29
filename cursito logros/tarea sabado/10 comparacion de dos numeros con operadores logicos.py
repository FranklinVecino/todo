#Ejercicio 10: Comparación de dos números con operadores lógicos

#Desarrolla un programa que solicite dos números y utilice operadores lógicos para verificar si ambos números son mayores que 10.
#El programa debe imprimir True si se cumple la condición y False en caso contrario.

print("\ningresa dos numeros y te dire si ambos son mayores a 10")

a = float(input("ingresa el primer numero: "))
b = float(input("ingresa el segundo numero: "))

c = (a > 10 and b > 10)
print(c)