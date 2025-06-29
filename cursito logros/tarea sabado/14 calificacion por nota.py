#Ejercicio 14: Calificación por nota

#Crea un programa que pida una calificación numérica del 1 al 100 y la convierta a una calificación alfabética, según la siguiente escala:

#90-100: A

#80-89: B

#70-79: C

#60-69: D

#Menos de 60: F


#><

n = int(input("ingresa tu nota y te dare una calificacion segun el alfabeto: "))

if (n > 0 and n < 100):
    
    if (n >= 90 and n <= 100):
        print("tu calificacion es: A.")
        
    elif (n >= 80 and n <= 89):
        print("tu calificacion es: B.")
        
    elif (n >= 70 and n <= 79):
        print("tu calificacion es: C.") 
           
    elif (n >= 60 and n <= 69):
        print("tu calificacion es: D.")
    
    else: print("tu calificacion es: F.")
    
else: print("el valor debe estar entre 0 y 100")

