#Ejercicio 4: Verificar si el año es bisiesto

#Escribe un programa que solicite un año y verifique si es un año bisiesto. Un año es bisiesto si es divisible por 4,
#excepto los años que son divisibles por 100 pero no por 400.

año = int(input("ingresa un año y te dire si es bisiesto o no"))

if año % 4 == 0:
    print("entonces es bisiesto")
    
elif año % 100 == 0:
    
    if año % 400 == 0:
        print("no es bisiesto")
        
    else: print("es bisiesto")

else: print("no es bisiesto")