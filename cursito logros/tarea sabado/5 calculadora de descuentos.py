#Ejercicio 5: Calcular el descuento en una compra

#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento. 
#El programa debe pedir el monto original de la compra y el porcentaje de descuento a aplicar.

print("soy tu calculadora de descuentos. porfavor ingresa el precio de tu compra y el descuento y te dire el precio final")

precio = float(input("ingresa el precio de tu compra en dolares: "))
descuento = int(input("ingresa el descuento a aplicar: "))

precio_descontado = precio * (descuento/100)
precio_final = precio - precio_descontado

print(f"el precio final de tu compra es $", precio_final,"gracias por su compra!!!")

