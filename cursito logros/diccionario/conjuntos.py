conjunto = {1,2,3,4,5,8}

print("\nmi conjunto es: ",conjunto)

print("\n¿ok el elemento 8 esta en el conjunto?", 8 in conjunto)

conjunto.add(6)
conjunto.add(7)
print("\nluego de las adiciones mi conjunto quedo asi: ", conjunto)

conjunto.discard(3)
conjunto.discard(90)
print("\nluego de eiliminar el 3 quedo asi: ",conjunto)

#ira recorriendo cada elemento para imprimirlo
for elemento in conjunto:
    print("\nelemento del conjunto: ", elemento)




# Añadir un elemento al conjunto
#mi_conjunto.add(6)  # Añade el número 6 al conjunto
#print("Conjunto después de añadir el número 6:", mi_conjunto)