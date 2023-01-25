def chistes_rojos():
    entrada = False
    print("Hola, mi nombre es Sebastian, y te contare algunos chistes rojos!!")
    print("""    
    Para continuar, presiona 'c' 
        
    Para salir, presiona 's'
    """)
    while not entrada:
      
        opcion = input(">> ")

        if opcion == "c":
            print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                  
    Un elefante se encuentra con un camello, y le pregunta:
    ■ ¿cómo es que tienes los pechos en la espalda?
    ► ¿y tú me lo preguntas, que llevas el miembro en la cara?
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■""")
            print("Ahi te va un chiste mas! (presiona intro para continuar)")
            input("    \n>> ")
            print("""   
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                 
    ■ Mamá, tengo dos noticias, una buena y una mala
    ► Primero la buena, hija.
    ■ Pasé una prueba.
    ► Muy bien, ¿Y la mala?
    ■ Que era un Test de embarazo...
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■""")
            print("    Deseas más chistes rojos? Indique 'si' o 'no'")
            
            a = False
            while not a:
                opcion2 = input("    >> ")
                if opcion2 == 'si':
                    print("""    
    Aqui tienes un par de chistes rojos extra...
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    
    ► Al final, he decidido hacerme la vasectomía
    ■ Habrá tenido que ser una decisión difícil ¿no?
    ► Ya lo creo. Hicimos una votación popular entre mis hijos,
      mi mujer y yo, y al final perdí por 16 a 17.
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    ► ¿Cuáles son las mujeres que mejor conocen su cuerpo?
    ■ Aquellas que se tocan, porque lo conocen al dedillo…
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                       
    ■ Una madre le dice a su hijo: ¡Me dice un pajarito que te drogas!
    ► La que se droga eres tú que habla con pajaritos!
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    """)
                    print("    Gracias por leer! :)")
                    input("""Presiona intro para regresar
    >> """)                
                    break
                if opcion2 == 'no':
                    print("""    
    Okiii, muchas gracias por leer, espero te hayas reido""")
                    break
                else:
                    print("""    Deseas más chistes inteligentes?
    Escriba 'si' o 'no' por favor
    """)
        if opcion == 's':
            print("Gracias Vuelve pronto...")
            break
        else:
            print("""                
    ► Para continuar, presiona 'c' 
        
    ► Para salir, presiona 's'
                  """)

chistes_rojos()