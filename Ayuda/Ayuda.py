
# *********************
# *********************
# Ayuda principal
# *********************
# *********************
class Ayuda:
    def Cordial(self):
        print("\nHola ^.^")
        print("Bienvenid@ a mi mundo de ayuda!!")
        print("\nDime o cuentame para que soy bueno")
        usuario = input()

    def mostrarOpciones(self):
        # Mostramos opciones
        print("\nHi!! mira solo en estos te puedo ayudar escoge sii")
        print("\n1. AYUDA PSICOLÓGICA") 
        print("2. AYUDA EN TAREA")
        print("0. VOLVER")


# *********************
# CLASE AYUDA DE TAREAS
# *********************
class AyudaTareas(Ayuda):
    def Cordial(self):
        print("\nHola, estas son la tareas que puedo realizar")

    def mostrarOpciones(self):
        print("\nAYUDIN NO, JAJA ESCOGE UNO HEE")
        print("1. APRENDER CANTANDO")
        print("2. Operacionescon matrices de 3 x 3")
        print("3. VOLVER")
        
        respuesta = int(input())

        if respuesta == 1:
            print("\nFísica es la ciencia natural con fundamentos que estudia "
                  "\nel universo, energía, Espacio - Tiempo propiedades de materia, "
                  "\ninteracción con movimiento de todo lo que rige en leyes de "
                  "\ncomportamientos está la mecánica cuántica y lo físico teórico"
                  "\nla clásica a lo macro y la moderna en microscópico. Puedes "
                  "\nver la matrix o vivir siempre con miedo, quejarte del mundo "
                  "\no aprender su juego .... Mi vida era escalar hasta que tope"
                  "\ncontigo se transformo en vector porque ahora tiene sentido. Todo "
                  "\ncuerpo existente puede sentir una fuerza con primera ley de"
                  "\nNewton se aplica la ley de inercia")
        elif respuesta ==2:
            while True:
                print('\n*************************************************')
                print('Este programa está hecho para una matriz de 3 x 3')
                print('*************************************************\n')
                print('Elige la Operción que deseas realizar: ')
                print('\n1. SUMA DE MATRICES'
                      '\n2. RESTA DE MATRICES'
                      '\n3. LA DIAGONAL DE UNA MATRIZ'
                      '\n4. LA MATRIZ TRANSPUESTA DE UNA MATRIZ'
                      '\n5. SALIR')
                opcion = int(input('opción deseada: '))
                 
                # SUMA DE MATRICES          
                if opcion == 1:
                             
                    matrizA = []
                    matrizB = []
                    matrizSuma = []
                             
                    # Agregando valores a la matriz A, Introducidos por el usuario
                    print('\nDatos para la matriz A')
                    for i in range (3):
                        pasaraA = []
                        for j in range(3):
                            datoA = int(input(f'numero para la fila {i+1} A: '))
                            pasaraA.append(datoA)
                        matrizA.append(pasaraA)

                    # Agregando valores a la matriz B, Introducidos por el usuario
                    print('\nDatos para la matriz B')
                    for i in range (3):
                        pasaraB = []
                        for j in range(3):
                            datoB = int(input(f'numero para la fila {i+1} B: '))
                            pasaraB.append(datoB)
                        matrizB.append(pasaraB)
                        
                    # Suma de la matriz A + B
                    for i in range(len(matrizA)):
                        sumaParcial= []
                        for j in range(len(matrizA[0])):
                            sum = matrizA[i][j] + matrizB[i][j]
                            sumaParcial.append(sum)
                        matrizSuma.append(sumaParcial)
                    
                    # Mostramos la matriz A
                    print('La matriz A: \n')
                    for linea in matrizA:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()
                          
                    # Mostramos la matriz B
                    print('La matriz B: \n')
                    for linea in matrizB:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()
                    
                    # Mostramos la matriz A +B
                    print('\nLa suma de la matriz A + B es: \n')
                    for linea in matrizSuma:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()
                                 
                # RESTA DE MATRICES             
                elif opcion == 2:
                    matrizA = []
                    matrizB = []
                    matrizResta = []

                    # Agregando valores a la matriz A, Introducidos por el usuario
                    print('\nDatos para la matriz A')
                    for i in range (3):
                        pasaraA = []
                        for j in range(3):
                            datoA = int(input(f'numero para la fila {i+1} A: '))
                            pasaraA.append(datoA)
                        matrizA.append(pasaraA)

                    # Agregando valores a la matriz B, Introducidos por el usuario
                    print('\nDatos para la matriz A')
                    for i in range (3):
                        pasaraB = []
                        for j in range(3):
                            datoB = int(input(f'numero para la fila {i+1} B: '))
                            pasaraB.append(datoB)
                        matrizB.append(pasaraB)
                    
                    # Hacemos la operación de resta de matrices
                    for i in range(len(matrizA)):
                        sumaParcial= []
                        for j in range(len(matrizA[0])):
                            sum = matrizA[i][j] - matrizB[i][j]
                            sumaParcial.append(sum)
                        matrizResta.append(sumaParcial)
                        
                    # Mostramos la matriz A
                    print('La matriz A: \n')
                    for linea in matrizA:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()
                        
                    # Mostramos la matriz B
                    print('La matriz B: \n')
                    for linea in matrizB:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()
                
                    # Mostramos la matriz A - B
                    print('\nLa resta de la matriz A - B es: \n')
                    for linea in matrizResta:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()
                        

                # LA DIAGONAL DE UNA MATRIZ
                elif opcion == 3:
                        
                    matrizA = []
                    diagonalMatriz = []
                    
                    # Agregando valores a la matriz A, Introducidos por el usuario
                    for i in range (3):
                        pasaraA = []
                        for j in range(3):
                            datoA = int(input(f'numero para la fila {i+1} A: '))
                            pasaraA.append(datoA)
                        matrizA.append(pasaraA)
                    
                    # Hallamos la matriz transpuesta
                    for i in range (len(matrizA)):
                        for j in range (len(matrizA[0])):
                            if i==j:
                                diagonalMatriz.append(matrizA[i][j])
                    # Mostramos la matriz
                    print('La matriz A: \n')
                    for linea in matrizA:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()
                    # Mostramos la diagonal de la matriz    
                    print('\nLa diagonal de la matriz A es: \n')
                    print(diagonalMatriz)
                # LA MATRIZ TRANSPUESTA DE UNA MATRIZ
                elif opcion == 4:
                    matrizA = []
                    matrizTranspuesta = []

                    # Agregando valores a la matriz A

                    for i in range (3):
                        pasaraA = []
                        for j in range(3):
                            datoA = int(input(f'numero para la fila {i+1} A: '))
                            pasaraA.append(datoA)
                        matrizA.append(pasaraA)

                    # Hallamos la transpuesta de la matriz

                    for i in range(len(matrizA[0])):
                        matrizAuxil = []
                        for j in range (len(matrizA)):
                            matrizAuxil.append(matrizA[j][i])
                        matrizTranspuesta.append(matrizAuxil)

                    # imprimimos la matriz

                    print('La matriz A: \n')
                    for linea in matrizA:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()

                    print('\nLa matriz transpuesta de A: \n')

                    #Imprimimos la matriz transpuesta
                    for linea in matrizTranspuesta:
                        for elemento in linea:
                            print(elemento, end =' ')
                        print()
            
                # SALIDA DEL PROGRAMA
                elif opcion == 5:
                    print('Gracias!')
                    break
                else:
                    print('\nOpción incorrecta!!')
                
        elif respuesta == 3:
            print("\nSmile 微笑 ^.^")
        else:
            print("\nEstimad@ ingrese el dato bien porfis")

# *********************
# *********************
# Ayuda psicologica
#************************************
class AyudaPsicologica(Ayuda):
    def Cordial(self):
        print("\nWELCOME, A LA ZONA DE ESTAR BIEN CON UNO MISMO!!")

    def mostrarOpciones(self):
        print("\n1. DESEAS QUE TE MOTIVE")
        print("2. AUTOCONOCERSE: CANCIÓN LETRAS")
        print("3. VOLVER")
        resta = int(input('Ingrese la opcion: '))
        if resta == 1:
            print("\nBueno mira asi como dice mis personajes favoritos de BTS:"
                  + "\nsolo tienes que seguir adelante, no pienses solo continua, no piense mucho lo que estas haciendo,"
                  + "\nluego un dia te darás cuenta que has crecido demasiado esa es la verdad para superar un bajón"
                  + "\nalgunas personas hacen sonar como si tuviera que hacer algo especial no es cierto solo tienes que"
                  + "\nseguir y no estes triste por no mejorar habrás mejorado antes de que te des cuenta."
                  + "\nDicen que es mas oscuro justo antes de que el sol salga. También las estrellas que adoras solo brillan"
                  + "\nen la noche. ¡Ánimo todo estará bien!. Te lo garantizo todo funcionara."
                  + "\nMira a qui tengo otras frases wooo"
                  + "\n1.Eres muy joven para dejar que el mundo te rompa. (Kin Taehyung)"
                  + "\n2. Nadie es feo solo vivimos en un mundo de criticas todos. (kin Nanjoon)"
                  + "\n3. Naciste para ser real. No perfecta. (Min Yoongi)"
                  + "\n4. Si hay alguien que no pueda ver hacia donde ir a partir de ahora le sugiero que escuche su corazón")
        elif resta == 2:
            print("'\nMe gusta, me gusta, me gusta,me gusta ser dinosaurio oh oh oh la la la"
                  + "\n¿Por qué quise esconder mi precioso ser de esta manera?, ¿De qué tenía tanto"
                  + "\nmiedo? ¿Por qué oculté mi verdadero yo? Soy yo a quien debo de amar woo woo oh"
                  + "\nen este mundo, iluminando mi preciosa alma finalmente me di cuenta que me amo no "
                  + "\ntan perfectamente, pero sí de un manera hermosa, soy a quien debo de amar"
                  + "\nA menudo las personas dicen que aún no se han encontrado a si mismas.Pero el si mismo no es algo")
        elif resta == 3:
            print("\nSmile 微笑 ^.^")
        else:
            print("\nEstimad@ ingrese el dato bien porfis")

# *********************
# *********************
def MostrarAyuda():
    #entrada = input('Ingrese un número: ')
    oAyuda = Ayuda()
    oAyudaPsicologica = AyudaPsicologica()
    oAyudaTareas = AyudaTareas()
    
    while True:
        oAyuda.Cordial()
        oAyuda.mostrarOpciones()
        entrada = input('Ingrese un número: ')
        rpt = int(entrada)
        print("**********")
        if rpt == 0:
            print("\nBueno seguro estarás bien Smile!!")
            break
        elif rpt == 1:
            oAyudaPsicologica.Cordial()
            oAyudaPsicologica.mostrarOpciones()
        elif rpt == 2:
            oAyudaTareas.Cordial()
            oAyudaTareas.mostrarOpciones()
        else:
            print("\nIngrese el dato bien")