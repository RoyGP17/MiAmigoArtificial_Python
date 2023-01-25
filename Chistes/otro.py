# valid_input = False
# while not valid_input:
#     user_input = input("Ingrese un número entero: ")
#     try:
#         user_input = int(user_input)
#         valid_input = True
#     except ValueError:
#         print("Entrada inválida, por favor ingrese un número entero.")
        

entrada = False
while not entrada:
    print("Hola, mi nombre es Sebastian, y te contare algunos chistes rojos!!")
    print("""    
    Para continuar, presiona 'c' 
    
    Para salir, presiona 's'
    """)
    ingresar = input("    >> ")
    try:
        ingresar = input(ingresar)
        if ingresar == 'c':
            print("""
        Un elefante se encuentra con un camello, y le pregunta:
        ■ ¿cómo es que tienes los pechos en la espalda?
        ► ¿y tú me lo preguntas, que llevas el miembro en la cara?
        """)
            print("Ahi te va un chiste mas! (presiona intro para continuar)")
            input("    >> ")
            print("""   
        ■ Mamá, tengo dos noticias, una buena y una mala
        ► Primero la buena, hija.
        ■ Pasé una prueba.
        ► Muy bien, ¿Y la mala?
        ■ Que era un Test de embarazo...
        """)
            print("    Deseas más chistes inteligentes? Indique 'si' o 'no'")
            entrada2 = False
            opcion = input("    >> ")
            if opcion == 'si':
                entrada2 = False
                while not entrada2:
                    try:
                        
                        print("""    
            Aqui tienes un chiste inteligente extra...
            
        ► Al final, he decidido hacerme la vasectomía
        ■ Habrá tenido que ser una decisión difícil ¿no?
        ► Ya lo creo. Hicimos una votación popular entre mis hijos,
          mi mujer y yo, y al final perdí por 16 a 17.
            """)
                        entrada = True
                        break
                    except ValueError:
                        print("Ingrese 'si' o 'no' por favor")
            if opcion == 'no':
                print("okii, espero te hayas reido")
                break
        entrada = True
        
    except ValueError:
        print("Entrada invalida, por favor ingrese 'si' o 'no'")
        