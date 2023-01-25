def chistes_blancos():
    entrada = False
    print("Hola, mi nombre es Lucy, y te contare algunos chistes blancos!!")
    print("""    
    Para continuar, presiona 'c' 
        
    Para salir, presiona 's'
    """)
    while not entrada:
      
        opcion = input(">> ")

        if opcion == "c":
            print("""
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                  
    ■ ¿Cuánto cuesta esta estufa?
    ► 6000 dolares
    ■ Pero, esto es una estafa
    ► No Señor, esto es una Estufa
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""")
            print("    Ahi te va un chiste mas! (presiona intro para continuar)")
            input("    \n>> ")
            print("""   
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                 
    ► YO VIVO A BASE DE VITAMINA C
    ■ Computador.
    ■ Celular.
    ■ Comida.
    ■ Cama.
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
    ► Estoy embarazada de ti
    ■ Eso es imposible, yo nací hace mucho tiempo        
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    ■ ¿Pasaste el examen de Química?
    ► NaH, ni de Bromo
    ■ ¿Estuvo dificil?
    ► Cloro que sí, Nitrato de hacerlo
    ■ Gracias 
    ► Acido un placer.
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                       
    ■ ¿Cómo se llama su hija?
    ► Esperanza
    ■ Imposible, La esperanza es lo último que se pierde
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    ■ ¡A MÍ NADIE ME DA ÓRDENES!
    ► “10% DE BATERÍA. CONECTE EL CARGADOR”
    ■ VOY.
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
""")
                    print("    Gracias por leer! :)")
                    input("""Presiona intro para regresar
    >> """)                
                    break
                if opcion2 == 'no':
                    print("""    
    Okiii, muchas gracias por leer, espero te hayas entretenido un rato""")
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

chistes_blancos()
            

    
           
   