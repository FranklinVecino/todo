#Ejercicio 15: Determinar si un número es positivo, negativo o cero

#Escribe un programa que solicite un número y determine si es positivo, negativo o igual a cero.

#><

n = float(input("ingrese un numero y le dire si es positivo, negativo o cero: "))

if (n > 0 ):
    print("el numero es positivo")

elif (n < 0):
    print("el numero es negativo")

else: print("el numero es cero")