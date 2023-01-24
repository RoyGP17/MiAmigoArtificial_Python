from datetime import date, timedelta

def Cumpleaños():
    # Crear un diccionario para almacenar nombres y fechas de cumpleaños
    cumpleanos = {
        "EDERSON": date(2004, 6, 27),
        "WILMER": date(1997, 6, 19),
        "ELVIS": date(1998, 12, 24),
        "LUCY": date(2002, 5, 30),
        "ROY": date(2001, 12, 6),
        "BICHENSO": date(2002, 7, 31),
        "LUIS": date(2002, 5, 14),
        "ANGUELO": date(2015, 12, 3)
    }

    # Pedir al usuario que ingrese su nombre
    nombre = input("Ingrese su nombre: ").upper()

    # Verificar si el nombre esta en el diccionario
    if nombre in cumpleanos:
        # Obtener la fecha de cumpleaños del usuario
        cumple = cumpleanos[nombre]

        # Calcular la fecha del próximo cumpleaños
        hoy = date.today()
        siguiente_cumple = date(hoy.year, cumple.month, cumple.day)
        if siguiente_cumple < hoy:
            siguiente_cumple = siguiente_cumple.replace(year=hoy.year + 1)
        # Calcular si el cumpleaño ya paso
        ya_paso = siguiente_cumple.year == hoy.year and siguiente_cumple < hoy
        # Calcular la diferencia en días entre hoy y el cumpleaños pasado
        dias_pasados = (hoy - cumple.replace(year=hoy.year)).days if ya_paso else 0
        # Calcular la diferencia en días entre hoy y el próximo cumpleaños
        dias_restantes = (siguiente_cumple - hoy).days
        # Mostrar al usuario los días que le quedan para su próximo cumpleaños o si su cumpleaño ya paso y los dias pasados
        if ya_paso:
            print(f"Su cumpleaño ya paso hace {dias_pasados} dias.")
        else:
            print(f"Hola! {nombre}, faltan {dias_restantes} dias para tu proximo cumpleaños.")
    else:
        print(f"{nombre} no esta registrado en nuestra base de datos.")
