
def recomendacion_gastronomica():
    print("\nMira que te puedo recomendar el "
          "\ntipo de comida de tu preferencia elije uno va.")
    opcion = 0
    while opcion != 3:
        print("\n1. Amazonicos")
        print("2. Criollos")
        print("3. volver")
        opcion = int(input("SELECCIONA UNA OPCION: "))
        if opcion == 1:
            print("ELIJA UNO DE LOS PLATOS AMAZONICOS: ")
            print("\t1. Tacacho con cecina")
            print("\t2. Crorixo con patacones")
            print("\t3. chaufa de cecina")
            print("\t4. Cecina a la parrilla")
            print("\t5. Yuca rellena")
            print("\t6. Juanes de gallina")
            print("\t7. Albondigas de cecina con chorizo")
            print("\t8. chaufa salvaje")
            print("\t9. chaufa de chorizo")
            print("\t10. Aeropuerto de cecina")
            print("\t11. Aeropuerto de chorizo")
            print("\t12. Pescado a lo macho")
            print("\t13. Jalea mixta amazonica")
            print("\t14. Carpacho de bagre")
            print("\t15. Carpacho de cabrilla")

            opcion1 = int(input("SELECCIONA UN PLATO: "))
            if opcion1 == 1:
                print("El precio de Tacacho con cecina es: " + "28.00"
                      + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 2:
                print("El precio de Crorizo con patacones es: " + "28.00"
                      + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 3:
                print("El precio de chaufa de cecina es: " + "20.00"
                      + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 4:
                print("El precio de Cecina a la parrilla es: " + "25.00"
                      + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 5:
                print("El precio de Yuca rellena es: " + "28.00"
                            + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 6:
                print("El precio de Juanes de gallina es: " + "30.00"
                            + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 7:
                print("El precio de Albondigas de cecina con chorizo es: " + "28.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 8:
                print("El precio de chaufa salvaje es: " + "20.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 9:
                print("El precio de chaufa de chorizo es: " + "20.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 10:
                print("El precio de Aeropuerto de cecina es: " + "30.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 11:
                print("El precio de Aeropuerto de chorizo es: " + "30.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 12:
                print("El precio de Pescado a lo macho es: " + "30.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 13:
                print("El precio de Jalea mixta amazonica es: " + "30.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 14:
                print("El precio de Carpacho de bagre es: " + "30.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion1 == 15:
                print("El precio de Carpacho de cabrilla es: " + "30.00"
                          + "\n te recomiendo ir a Rustica.Br")
            elif opcion == 16:
                print("OPCION INCORRECTA")

        elif opcion == 2:
            print("ELIJA UNO DE LOS PLATOS CRIOLLOS: ")
            print("\t1. Arroz con pato")
            print("\t2. Arroz con pollo")
            print("\t3. Carapulcra")
            print("\t4. Pachamanca")
            print("\t5. Olluquito con charqui")
            print("\t6. Hornado con mote")
            print("\t7. Guiso de faso con chancho")
            print("\t8. Chanfainita")
            print("\t9. Ceviche")
            print("\t10. Lomo saltado")
            print("\t11. Volver")

            opcion2 = int(input("\tSELECCIONA UN PLATO: "))
            if opcion2 == 1:
                print("El precio de Arroz con pato es: " + "30.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 2:
                print("El precio de Arroz con pollo es: " + "25.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 3:
                print("El precio de Carapulcra es: " + "28.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 4:
                print("El precio de Pachamanca es: " + "30.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 5:
                print("El precio de Olluquito con charqui es: " + "28.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 6:
                print("El precio de Hornado con mote es: " + "28.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 7:
                print("El precio de Guiso de faso con chancho es: " + "30.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 8:
                print("El precio de Chanfainita es: " + "25.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 9:
                print("El precio de Ceviche es: " + "25.00"
                          + "\n te recomiendo ir a El Hornito.Br")
            elif opcion2 == 10:
                print("El precio de Lomo saltado es: " + "25.00"
                          + "\n te recomiendo ir a El Hornito.Br")
        elif opcion == 3:
            break
        else:
            print("Opcion invalida")
    print("Usted ha terminado las acciones de la recomendacion gastronomica")

