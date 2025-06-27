n = input("ingresa el num")

if n < 0:
    print("es negativo")

    if n % 2 == 0:
        print("tu numero es negativo y par")
    else: print("es negativo e impar")

elif n > 0:
    print("es positivo")

    if n % 2 == 0:
        print("tu numero es positivo y par")
    else: print("es positivo e impar")

else: print("es cero")