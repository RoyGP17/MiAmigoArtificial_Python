
def saludar():
    print("\n\tPROJETCS: MI AMIGO ARTIFICIAL")
    print("\nFui creado el año 1969 fecha en la que el hombre dio un salto"
          "\nPero no de un salto, sino un salto de la humanidad del hombre vale.")

def adivinar_edad():
    print("\nMira te digo, Que soy increible adivinando tu edad "
          "\ny apuesto que lo haré, asi que comenzamos")
    print("Cúal es el resto al dividir tu edad por 3: ")
    resto3 = int(input())
    print("Ahora cúal es el resto al dividir tu edad por 5: ")
    resto5 = int(input())
    print("Finalmente cúal es el resto al dividir tu edad por 7: ")
    resto7 = int(input())
    edad = (resto3 * 70 + resto5 * 21 + resto7 * 15) % 105
    print(f"\nhaciendo un esfuerzo mental y mis fabulosos cálculos"
          f"\nMe arroja que tu edad es {edad} y de hecho somos compatibles asi como"
          f"\nel signo nega y posi")

def despedida():
    respuesta1 = input("\nYa te vas, tan pronto?: si/no").upper()
    if respuesta1 == "SI":
        print("\nQue tengas un lindo día, cuidate mucho"
              "\nmi querido amigo, me encanto ser tu amigo "
              "\nen estos mil años de aventura <3")
    else:
        respuesta2 = input("Desea ver un lindo gatito? si/no").upper()
        if respuesta2 == "SI":
            print("Gatito")
            breakpoint()