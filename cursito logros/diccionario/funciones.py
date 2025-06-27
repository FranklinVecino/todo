#se definicion y ejecucion de una funcion que calcule el area de un circulo, pide el radio y muestra tanto su area como su radio
def area_del_circulo(radio):
    """explicacion"""
    import math
    return math.pi * (radio ** 2)

radio =5
area = area_del_circulo(radio)
print(f"el radio que me diste es:",radio,"y su area en metros es:",area)







#def calcular_area_del_circulo(radio):
#    """calcular el area de un circulo"""
#    import math 
#    return math.pi * (radio ** 2)


#radio = 5
#area = calcular_area_del_circulo(radio)
#print(f"El área de un círculo de radio {radio} es: {area:.2f}")










#def calcular_area_circulo(radio):
#    """Función que calcula el área de un círculo."""
#    import math  # Importa el módulo math para usar la constante pi
#    return math.pi * (radio ** 2)  # Calcula el área usando la fórmula π * r^2
