#Ejercicio 3: Comparar dos números

#Desarrolla un programa que pida al usuario dos números y muestre cuál de los dos es mayor, o si son iguales.

n1 = float(input("ingresa un numero"))
n2 = float(input("ingresa otro numero"))

if n1 > n2:
    print("el primer numero ingresado es mayor")

elif n2 > n1:
    print("el segundo numero es mayor")

else: print("ambos numeros son iguales")

