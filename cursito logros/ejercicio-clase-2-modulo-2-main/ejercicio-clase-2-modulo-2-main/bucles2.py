#Control de Bucles (break).py Crea un bucle for que itere sobre los números del 1 al 10. 
# El bucle debe detenerse e imprimir "Número encontrado" cuando el número sea 7, utilizando 
# la sentencia break.

for num in range(11):
    print("el numero es:", num)
    if num == 7:
        print("numero encontrado")
        break