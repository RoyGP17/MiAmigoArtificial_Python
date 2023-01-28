class libro:
    def __init__(self, autor, nombre, genero, resumen):
        self.autor = autor
        self.nombre = nombre
        self.genero = genero
        self.resumen = resumen

    # METODOS ACCESORES

    def Get_autor(self):
        return self.autor

    def set_autor(self, autor_modificado):
        self.autor = autor_modificado

    def Get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre_modificado):
        self.autor = nombre_modificado

    def Get_genero(self):
        return self.genero

    def set_genero(self, genero_modificado):
        self.genero = genero_modificado

    def Get_resumen(self):
        return self.resumen

    def set_autor(self, resumen_modificado):
        self.resumen = resumen_modificado

    def intrudcion(self):
        print(f"Tenemos: {self.nombre} es un obra de: {self.genero} escrito por {self.nombre} ")

    def leer_libro(self):
        print(self.Get_resumen())
        print("Lucho")


### TODAS LAS HERENCIAS

## CLASE LIBRO AVENTURA ##
## Clase clonada ###

class libroAventura(libro):

    def __init__(self, autor, nombre, genero, resumen):
        super().__init__(autor, nombre, genero, resumen)

    def leer_libro(self):
        print(self.Get_resumen)

        print(
            "tengo para ti:\n \t\nUn libro de Aventura que emocionante " + self.Get_nombre() + "\nEscrito por: " + self.Get_autor())


###LIbro Comedia ####

class libroComedia(libro):
    def __init__(self, autor, nombre, genero, resumen):
        super().__init__(autor, nombre, genero, resumen)

    def leer_libro(self):
        print(self.Get_resumen)

    def intrudcion(self):
        print(
            "tengo para ti:\n \t\nUn libro de Comedia apuesto que te sacará una sonrrisa " + self.Get_nombre + "\nEscrito por: " + self.Get_autor)


## Libro Drama ####

class libroDrama(libro):

    def __init__(self, autor, nombre, genero, resumen):
        super().__init__(autor, nombre, genero, resumen)

    def leer_libro(self):
        print(self.Get_resumen)

    def intrudcion(self):
        print(
            "tengo para ti:\n \t\nUn libro de Aventura que emocionante " + self.Get_nombre() + "\nEscrito por: " + self.Get_autor())
