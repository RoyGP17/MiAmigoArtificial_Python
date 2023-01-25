import random

from Tools.scripts.var_access_benchmark import A


class Admin_Libros:

    def __init__(self):
        self.listaLibrosDeDrama = [None] * 10
        self.listaLibrosDeComedia = [None] * 10
        self.listaLibrosDeAventura = [None] * 10

    def agrega_libro(self, nombre, genero, orden):

        if genero == "Drama":
            self.listaLibrosDeDrama[orden] = nombre

        if genero == "Comedia":
            self.listaLibrosDeDrama[orden] = nombre

        if genero == "Aventura":
            self.listaLibrosDeDrama[orden] = nombre

        else:
            print("No existe esa opcion intente nuevamente")

    def menu(self):
        print("Hola :) Elige una de la opciones: ")
        print("1-----> Libros ")
        print("2-----> Volver")

        respuesta = int(input())

        if respuesta == 1:
            print(
                "Bienbenid@ al mundo de los libros, echemos un vistaso a lo que tenemos:\n viajemos al interior de tu mente")

            respuesta1 = False

            while not respuesta1:
                print("Te presento las siguintes Bibliotecas")
                print("1----->Dramas")
                print("2----->Aventuras")
                print("3----->Comedias")
                print("4----->(VOLVER)")

                if respuesta1 == 1:

                    aleatoria = random.randint(0, 3)

                    self.listaLibrosDeDrama[aleatoria].intrudcion()
                    self.listaLibrosDeDrama[aleatoria].leer_libro()

                    print("Al parecer esta lloviendo pipipip :( ")

                elif respuesta1 == 2:

                    aleatoria = random.randint(0, 3)

                    self.listaLibrosDeAventura[aleatoria].intrudcion()
                    self.listaLibrosDeAventura[aleatoria].leer_libro()
                    print("WOW es muy increible no lo crees: ")

                elif respuesta1 == 3:
                    aleatoria = random.randint(0, 3)

                    self.listaLibrosDeComedia[aleatoria].intrudcion()
                    self.listaLibrosDeComedia[aleatoria].leer_libro()
                    print("!JAJAJAJAJA , fue muy chistoso que me dule el estamgo XD ")

                elif respuesta1 == 4:
                    print("Bueno ¿ya te vas?, Bye cuidate nos vemos pronto :)")

                else:
                    print("#Error : Lo siento vuelve a intentarlo....")

        else:
            print("#Error : Lo siento vuelve a intentarlo....")
