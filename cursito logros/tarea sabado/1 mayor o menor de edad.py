#Ejercicio 1: Mayor de edad

#Escribe un programa que le pida al usuario su edad y determine si es mayor de edad o no. 
# Considera que la mayoría de edad se alcanza a los 18 años.

edad = int(input("ingresa tu edad:"))

if edad >= 18:
    print("eres mayor de edad")
elif edad >= 1:
    print("eres menor de edad")
    
else: print("introduciste una edad invalida")