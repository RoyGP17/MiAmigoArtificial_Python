def chistes_inteligentes():
    entrada = False
    print("Hola, mi nombre es Rocotito, y te contare algunos chistes inteligentes!!")
    print("""    
    Para continuar, presiona 'c' 
        
    Para salir, presiona 's'
    """)
    while not entrada:
      
        opcion = input(">> ")

        if opcion == "c":
            print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                  
    ■ Que bonito es hacer el amor cuando tus hijos estan en el colegio
    ► Pero si tu no tienes mujer ni hijos
    ■ Creo que no me estas entendiendo...
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""")
            print("    Ahi te va un chiste mas! (presiona intro para continuar)")
            input("    \n>> ")
            print("""   
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                 
    ► Por que se mira primero el rayo luego se escucha el sonido?
    ■ Porque los ojos estan delante de los oidos...
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""")
            print("    Deseas más chistes inteligentes? Indique 'si' o 'no'")
            
            a = False
            while not a:
                opcion2 = input("    >> ")
                if opcion2 == 'si':
                    print("""    
    Aqui tienes un par de chistes inteligente extra...
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    
    ► La luz viaja más rápido que el sonido. Por eso mucha gente
      parece brillantes hasta que lo oyes hablar             
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    ■ Mi papá vive de las letras
    ► Ah, ¿es escritor?
    ■ No, sufre de diabetes y vive tomando vitaminas A, B, C, D.
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

chistes_inteligentes()







        
