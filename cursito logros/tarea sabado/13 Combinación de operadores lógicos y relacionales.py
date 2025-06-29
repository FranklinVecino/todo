#Ejercicio 13: Combinación de operadores lógicos y relacionales

#Desarrolla un programa que pida un número al usuario y determine si dicho número es par y si se encuentra en el rango de 20 a 50.


print("combinare tanto operadores logicos como condicionales")

n = int(input("dame un numero: "))

if n % 2 == 0:
    
    if n >= 20 and n <= 50:
        print("es par y tambien esta entre 20 y 50")
        
    else: print("es par, pero no esta entre 20 y 50")
    
elif n >= 20 and n <= 50:
    print("es impar pero esta dentro del rango")
    
else: print("no es par ni esta dentro del rango")