from Gastronomico import recomendacion_gastronomica
from Academico import recomendacion_academica
def recomendacion():
    print("\n\tBIENVENIDO A LA SECCION DE RECOMEDACIONES")

    while True:
        print("1. Recomendacion gastronómica")
        print("2. Recomendacion académica")
        print("3. Volver")

        opcion_de_entrada = int(input("POR FAVOR ELIJA UNA OPCION: "))
        if opcion_de_entrada == 1:
            recomendacion_gastronomica()
            break
        elif opcion_de_entrada == 2:
            recomendacion_academica()
            break
        elif opcion_de_entrada == 3:
            print("Vuelve prontoo!!")
            break
        else:
            print("OPCION INCORRECTA!")

    print("Usted ha terminado las acciones de la recomendacion")




