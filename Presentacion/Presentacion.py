def saludar():
    print("\n\tPROJETCS: MI AMIGO ARTIFICIAL")
    print("""
               Fui creado el año 1969 fecha en la que el hombre dio un salto 
               Pero no de un salto, sino un salto de la humanidad del hombre vale""")

def adivinar_edad():
    print("\nMira te digo, Que soy increible adivinando tu edad y apuesto que lo haré")
    print("Asi que comenzamos")
    print("Cúal es el resto al dividir tu edad por 3: ")
    resto3 = int(input())
    print("Ahora cúal es el resto al dividir tu edad por 5: ")
    resto5 = int(input())
    print("Finalmente cúal es el resto al dividir tu edad por 7: ")
    resto7 = int(input())
    edad = (resto3 * 70 + resto5 * 21 + resto7 * 15) % 105
    print("haciendo un esfuerzo mental y mis fabulosos cálculos")
    print(f"Me arroja que tu edad es {edad} y de hecho somos compatibles asi como")
    print("el signo nega y posi")
