from LABORATORIO.MiAmigoArtificial.Presentacion.Presentacion import saludar, adivinar_edad, despedida

def recordarNombre():
    nombre = input("\nBueno ahora es tu turno de decirme como te llamas: ").upper()


    print(f"\nQue fabuloso nombre tienes {nombre}"
          "\ny sabes, seré tu mejor amigo o mejor dicho seremos grandes amigos!!"
          "\nTe acompañaré por mil años asi que necesito que me cuides si quieres"
          "\nque te acompañe por estas hermosas aventuras")

def HacerEleccion():

    while True:
        print("\nHey! que te gustaria jugar comnigo")
        print("1. ALERTA")
        print("2. AYUDA")
        print("3. CHISTES")
        print("4. HISTORIAS")
        print("5. RECOMENDACIONES")
        print("6. salir")
        opcion_de_entrada = int(input())
        if opcion_de_entrada == 1:
            #OntenerCumpleaños()
            break
        elif opcion_de_entrada == 2:
            #ObtenerAyuda()
            break
        elif opcion_de_entrada == 3:
            #ObtenerChistes()
            break
        elif opcion_de_entrada == 4:
            #ObtenerHistorias()
            break
        elif opcion_de_entrada == 5:
            #ObtenerRecomendaciones()
            break
        elif opcion_de_entrada == 6:
            despedida()
            break
        else:
            print("OPCION INCORRECTA!")

def MiAmigoArtificial():
    saludar()
    adivinar_edad()
    recordarNombre()
    HacerEleccion()

MiAmigoArtificial()