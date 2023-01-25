import importlib
def chistes():
    while not False:
        print("BIENVENIDOS AL MUNDO DE LOS CHISTES")
        print("1. Chistes Blancos")
        print("2. Chistes Buenos")
        print("3. Chistes Inteligentes") 
        print("5. VOLVER")
        opcion = int(input("Ingresa una opcion:"))
        if opcion == 1:
            importlib.import_module('chistes_blancos')
            return
        if opcion == 2:
            importlib.import_module('chistes_buenos')
        if opcion == 3:
            importlib.import_module('chistes_inteligentes')
        if opcion == 4:
            importlib.import_module('chistes_rojos')
        if opcion ==5:
            print("Gracias, te espero aqui siempre :)")
            break
        else:
            print("""
Ingrese una opcion valida por favor        
""")
