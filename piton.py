#explicaciion corta de como funciona mi programa

    #primero se encarga de mostrar un menu con opciones donde el usuario elige al introducir un numero y se ejecuta la 
    #funcion esperada.

    #agg = pide nombre y precio y lo añade a la cesta
    #mostrar = lista todos los elementos y su respectivo precio
    #eliminar = muestra la lista y permite eliminar por numero 
    #calc = suma todos los precios de los productos
    #renuncia = salir


def mostrar_menu():
    print("\nMenu:")
    print("1. agregar un nuevo producto o servicio")
    print("2. mostrar el contenido de la cesta de la compra")
    print("3. eliminar un producto")
    print("4. para Calcular el total")
    print("5. para salir del programa")


# funcion agregar elemento a la cesta. pide al usuario el elemento y luego hace una pequeña revision de que no este mal lo que se ingresa

def agregar_producto(cesta):
    producto = input("introduce el nombre del producto a agregar: ")

    try:
        precio = float(input("introduce el precio del producto: "))
    except ValueError:
        print("Precio invalido. Por favor, introduce un numero.")
        return
    
    cesta.append({"nombre": producto, "precio": precio})
    print(f"producto '{producto}' agregado con precio {precio:.2f}.")




# funcion que muestra el contenido de la cesta y que usa un bucle for para poder mostrar los productos enumerados y con su precio en dolares
#con dos decimales

def mostrar_cesta(cesta):
    if not cesta:
        print("La cesta esta vacia.")
        return
    print("Contenido de la cesta:")
    for i, item in enumerate(cesta, 1):
        print(f"{i}. {item['nombre']} - ${item['precio']:.2f}")



#funcion para eliminar los productos, si no hay nada en la cesta lo indica

def eliminar_producto(cesta):
    if not cesta:
        print("La cesta esta vacia. No hay producto para eliminar.")
        return
    mostrar_cesta(cesta)
    try:
        indice = int(input("Introduce el numero del producto a eliminar: "))
        if 1 <= indice <= len(cesta):
            eliminado = cesta.pop(indice - 1)
            print(f"producto '{eliminado['nombre']}' eliminado.")
        else:
            print("numero invalido.")
    except ValueError:
        print("Entrada invalida. Por favor introduce un numero.")



def calcular_total(cesta):
    total = sum(item["precio"] for item in cesta)
    print(f"El total de la cesta es: ${total:.2f}")


#nucleo del programa:
def main():
    cesta = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            agregar_producto(cesta)
        elif opcion == "2":
            mostrar_cesta(cesta)
        elif opcion == "3":
            eliminar_producto(cesta)
        elif opcion == "4":
            calcular_total(cesta)
        elif opcion == "5":
            print("Gracias por usar el programa. Hasta luego")
            break
        else:
            print("opcion no valida. Por favor, elige una opción del menu.")



#al ejecutar el archivo, se llama a la funcion main para iniciar al programa
#es para que el codigo sea exportable sin que se ejecute automaticamente

if __name__ == "__main__":
    main()
