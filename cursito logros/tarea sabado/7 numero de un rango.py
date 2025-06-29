#Ejercicio 7: Número dentro de un rango

#Escribe un programa que verifique si un número ingresado por el usuario se encuentra dentro de un rango específico 
#(por ejemplo, entre 10 y 50). Deberás solicitar el número y luego indicar si está o no dentro del rango.

n  = float(input("ingresa un numero y te dire si entra dentro de mi rango"))

if n >= 10 and n <= 100:
    print("estas dentro del rango")

else: print("te saliste del rango")