from Animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    listado = []

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_escamas=None, cantidad_aletas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.__color_escamas = color_escamas
        self.__cantidad_aletas = cantidad_aletas
        Pez.listado.append(self)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez.salmones += 1
        return cls(nombre, edad, "océano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez.bacalaos += 1
        return cls(nombre, edad, "océano", genero, "gris", 6)

    @classmethod
    def cantidad_peces(cls):
        return len(cls.listado)