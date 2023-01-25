from Cumpleaños import Cumpleaños
from WhatsAap import WhatsApp

def Alerta():
    while True:
        print("\nHey mas despacio! estas en el mundo de las alertas")
        print("1. CUMPLEAÑOS")
        print("2. WHATSAPP")
        print("3. salir")
        opcion_de_entrada = int(input())
        if opcion_de_entrada == 1:
            Cumpleaños()
            break
        elif opcion_de_entrada == 2:
            WhatsApp()
            break
        elif opcion_de_entrada == 3:
            print("Vuelve prontoo!!")
            break
        else:
            print("OPCION INCORRECTA!")
