from Alerta import Alerta
from Ayuda import MostrarAyuda
from Presentacion import despedida, saludar, adivinar_edad
from chistes import chistes
from Recomendacion import recomendacion
from Historia import Historias
print("HOLA")


def recordarNombre():
    nombre = input("\nBueno ahora es tu turno de decirme como te llamas: ").upper()


    print(f"\nQue fabuloso nombre tienes {nombre}"
          "\ny sabes, seré tu mejor amigo o mejor dicho seremos grandes amigos!!"
          "\nTe acompañaré por mil años asi que necesito que me cuides si quieres"
          "\nque te acompañe por estas hermosas aventuras")
def ObtenerHistorias():
    oHistoria = Historias()
    oHistoria.leer_libro()

def HacerEleccion():

    while True:
        print("\nHey! que te gustaria jugar comnigo")
        print("1. ALERTA")
        print("2. AYUDA")
        print("3. CHISTES")
        print("4. HISTORIAS")
        print("5. RECOMENDACIONES")
        print("6. salir")

        opcion_de_entrada = int(input("Elige una de las opciones: "))
        while opcion_de_entrada !=0:
            if opcion_de_entrada == 1:
                Alerta()
                break
            elif opcion_de_entrada == 2:
                MostrarAyuda()
                break
            elif opcion_de_entrada == 3:
                chistes()
                break
            elif opcion_de_entrada == 4:
                ObtenerHistorias()
                break
            elif opcion_de_entrada == 5:
                recomendacion()
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
