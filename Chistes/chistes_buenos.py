def chistes_buenos():
    entrada = False
    print("Hola, mi nombre es Lucy, y te contare algunos chistes buenos!!")
    print("""    
    Para continuar, presiona 'c' 
        
    Para salir, presiona 's'
    """)
    while not entrada:
      
        opcion = input(">> ")

        if opcion == "c":
            print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                  
    ■ Qué detalle, tu mujer murió hace 4 años, y tu sigues preparando 
      la mesa para cenar, como si aun estuviese.
    ► Qué va, lo que pasa es que no tengo ganas de recoger
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""")
            print("    Ahi te va un chiste mas! (presiona intro para continuar)")
            input("    \n>> ")
            print("""   
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                 
    ► Paciente: Doctor, me duele aquí.
    ■ Doctor: Pues póngase allí.
    ► Paciente: Doctor, me sigue doliendo.
    ■ Doctor: Doliendo, deje de seguir al paciente.
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
    ► Paciente: Doctor, me duele cuando hago asi.
    ■ Doctor: Entonces no haga asi, saludos jajaja...         
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    ■ Le dice el niño a la madre: Mamá, no quiero jugar más con Pedrito. 
      La madre le pregunta al niño:
    ► ¿Por qué no quieres jugar más con él?
    ■ porque cuando jugamos a los tacos de madera y le pego con uno en la 
      cabeza, de repente se pone a llorar.
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                       
    ■ ¿Cuáles son las mujeres que mejor conocen su cuerpo?
    ► Aquellas que se tocan, porque lo conocen al dedillo
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    ■ ¿Cómo se llama el primo de Bruce Lee? 
    ► Broco Lee.
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

chistes_buenos()







