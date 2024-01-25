print("""Entras a un cuarto oscuro con dos puertas.
¿Qué puerta abrirías? ¿#1 o #2?""")

door = input("> ")

if door == "1":
    print("Abrirás la puerta #1...")
    print("En este cuarto hay un oso gigante comiéndose un pastel")
    print("¿Qué harás?")
    print("a. Tomar el pastel")
    print("b. Gritarle muy fuerte al oso")
    
    bear = input("_ ")
    
    if bear == "a":
        print("El oso te come. Fin del juego")
    elif bear == "b":
        print("El oso se pone furioso y te ataca. Fin del juego")
    else:
        print("Bien hecho. Has dejado al oso en paz y este ha huído.")
        print("Avanzas por el calabozo")
    
elif door == "2":
    print("Abrirás la puerta #2...")
    print("Has entrado a la guarida del mago oscuro")
    print("Te reta a un duelo. ¿Qué harás?")
    print("#: Lanzar abracadabra")
    print("!: Lanzar hechizo de escudo")
    print("?: Comerme un \"snickers\"")
    
    
    wizard = input("+ ")
    
    # TODO: definir este caso
else:
    print("Haz caído en una trampa. Estás muerto")
