from Lista import lista_carreras_unsch, lista_carreras_unsaac


def recomendacion_academica():

    while True:
        print("\nHey! mi querico amigo, estas en la seccion de "
                    + "\nrecomendaciones academicas, estas son las posibles recoemndaicones "
                    + "\nque te puedo brindar ahora.")
        print("ELIGE UNA OPCION:")
        print("1) Elija esta opcion si presenta posibles problemas academicos")
        print("2) Elige esta opcion para brindarte recomendaciones"
                    + "\nde las carreras universitarias")
        print("3) volver")

        opcion = int(input("SELECCIONA UNA OPCION: "))
        if opcion == 1:
            print("Dime! que te puedo recomendar")
            print("1. Problemas de concentracion")
            print("2. Falta de organizacion")
            print("3. Inseguridad en el desarrollo academico")
            print("4. volver")

            opcion1 = int(input("SELECCIONA UNA OPCION: "))
            if opcion1 == 1:
                print("\nSe te hace muy dificil al no pensar "
                            + "\nen otra cosa mientras intenta prestar atencion, "
                            + "\n pues yo te recomiendo ser dinamico en las "
                            + "\n clases con esto me refiero a que siempre "
                            + "\npregunta a tu maestro por algun minimo detalle")
            elif opcion1 == 2:
                print("\nLe genera estres o descuido total de las "
                            + "\nactividades, si este problema no es tratado suele "
                            + "\nllevarse hasta la edad adulta. Tranquilo "
                            + "\nmi querido amigo estoy aqui para recoemdarte lo "
                            + "\nsiguente, revisa tus objetivos trazados, leer "
                            + "\nun libro sobre el manejo del tiempo, arma tu "
                            + "\nagenda con anticipacion y posteriormente divive "
                            + "\nlos deberes del dia por secciones de tiempo.")
            #
            elif opcion1 == 3:
                print("\nSientes que no eres capaz aun cuando te has "
                            + "\npreparado para realizar un examen, exposicion o cualquier "
                            + "\notro tipo de actividad, talvez hasta puedes ser inseguro "
                            + "\nen la entrega adecuadad de una materia"
                            + "\nEntonces te recomiendo cambiar tus "
                            + "\npensamientos por unos que sean positivos, y recuerda "
                            + "\nque nadie es perfecto, tal cosa como la pefeccion no existe"
                            + "\ndiviertete, deja de compararte y conversa con una persona "
                            + "\nque sientas que es de confianza")
            elif opcion1 == 4:
                break
            else:
                print("Elija una opcion correcta")
        elif opcion == 2:
            print("\nOye! te recomiendo estas carreras... estas son las carreras universitarias "
                  "\nm??s populares y con mayor demanda en el mercado laboral actualmente:")
            print("- Ingenier??a en Sistemas")
            print("- Administraci??n de Empresas")
            print("- Contadur??a")
            print("- Psicolog??a")
            print("- Ingenier??a Civil")
            print("- Medicina")
            print("- Ingenier??a Qu??mica")
            print("- Ingenier??a Industrial")
            print("- Ingenier??a El??ctrica")
            print("- Ingenier??a de Software")
            print("\nTen en cuenta que estas recomendaciones pueden variar dependiendo de la situaci??n "
                  "\necon??mica y el mercado laboral en tu pa??s o regi??n. Es importante investigar "
                  "\ny hacer una elecci??n informada antes de elegir una carrera universitaria.")
            entrada = input("\n??Deseas ver las carreras de algunas universidades? si/no : ").upper()
            if entrada == "SI":
                    print("\nA continuacion puedo mostrarte algunas carreras de las universidades como "
                          "\nla UNSCH Y LA UNSAAC de nuestro pais.")
                    print("1. Carreras de la Universidad Nacional de San Cristobal de Huamanga")
                    print("2. Carreras de la Universidad Naciona de San Antonio de Abad del cusco")
                    entrada2 = int(input("SELECCIONA UNA OPCION: "))
                    if entrada2 == 1:
                        lista_carreras_unsch()
                    elif entrada2 == 2:
                        lista_carreras_unsaac()
                    else:
                        print("OPCION INCORRECTA")
            else:
                print("\nHata luego y recuerda estudiar lo que mas te gusta hacer!!")
        elif opcion == 3:
            break
        else:
            print("Elija una opcion correcta")