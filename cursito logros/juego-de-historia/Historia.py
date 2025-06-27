print("\nBienvenido al juego de astronomía, eres un astronauta, en una de tus misiones rutinarias descubres un nuevo planeta")
print("Debes tomar la decision correcta para manejar este descubrimiento que has hecho")

print("\n¿que opcion eliges?:")
print("1 investigar el planeta de cerca")
print("2 informar a la comunidad cientifica sobre tu descubrimiento")

opcion = int(input("\nelige: "))

#elige investigar
if opcion == 1:
    print("\ninvestigas el planeta, no estas seguro de como proceder, notas que la atmosfera es mas densa que en la tierra, y su gravedad tambien es mas fuerte")
    print("tu nave tiene poco combustible pero ves la oportunidad de estudiar el planeta a pesar de los riesgos")
    
    print("\n¿que opcion eliges?:")
    print("1 tomar muestras del entorno arriesgandose")
    print("2 no arriesgarse y volver a estudiarlo desde la tierra")
    
    opcion = int(input("\nelige: "))
    
    #se arriesga FIN
    if opcion == 1:
        print("tomas muestras de la atmosfera y con ello descubres que contiene oxigeno, entre otros gases")
        print("gracias al riesgo que tomaste has hecho un gran descubrimiento. el planeta podria ser habitable. !fin del juego¡")
        
    #no se arriesga FIN
    elif opcion == 2:
        print("vuelves sano y salvo, y desde la comodidad de la tierra analizas el planeta, pero los datos obtenidos no son concluyentes")
        print("es imposible determinar si el planeta es habitable o no. !fin del juego¡")
    else: ("opcion invalida")      
    
elif opcion == 2:
    print("\ninformas a la comunidad cientifica sobre tu avistamiento, estos organizan una mision para explorar dicho planeta")
    print("puedes formar parte del equipo encargado de esta mision para colaborar con el descubrimiento.")
    
    print("\n¿que opcion eliges?:")
    print("1 unirte a la mision")
    print("2 investigar desde la tierra")
    
    opcion = int(input("\nelige: "))
    
    #te unes a la mision
    if opcion == 1:
        print("decides unirte a la mision, junto al equipo de cientificos descubres vida microbiana en el planeta")
        print("haz cambiado la historia de la astronomica para siempre. !fin del juego¡")
        
    #no te unes a la mision
    elif opcion == 2:
        print("decides quedarte en la tierra y sigues investigando")
        print("contribuyes a la comunidad cientifica con pequeños aportes. !fin del juego¡")
    else: ("opcion invalida")     
    
        
else: ("opcion invalida")