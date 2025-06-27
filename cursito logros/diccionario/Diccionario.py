diccionario = {

    "liliana" : 21,
    "carlos" : 20,
    "elias" : 22,
    "damian" : 21,
    "arianyela" : 20,
    "jelyanirr" : 22,
}

print("\n",diccionario)

diccionario["liliana"] = 15
diccionario["carlos"] = 18
diccionario["elias"] = 20
diccionario["damian"] = 12
diccionario["arianyela"] = 15
diccionario["jelyanirr"] = 17

print("\ntu nuevo diccionario es: ",diccionario)

print("\n¿la clave 'carlos' esta en el diccionario?", "carlos" in diccionario)

for elias in diccionario:
    print(f"\nnombre: {elias}, nota: {diccionario[elias]}")

for nota in diccionario.values():
    print("nota:",nota)

# Iterar sobre las claves del diccionario
#for clave in mi_diccionario:
# #   print(f"Clave: {clave}, Valor: {mi_diccionario[clave]}")  # Imprime cada clave y su valor asociado



# Comprobar si una clave está en el diccionario
#print("¿La clave 'nombre' está en el diccionario?", "nombre" in mi_diccionario)  # Comprueba si la clave "nombre" existe en el diccionario

#mi_diccionario["edad"] = 31  # Cambia el valor asociado a la clave "edad"
#print("Diccionario después de modificar la edad:", mi_diccionario)




#diccionario = {

#    "nombre" : "juan",
#    "edad" : 30,
#    "ciudad" : "madrid"

#}

#print("\n",diccionario)