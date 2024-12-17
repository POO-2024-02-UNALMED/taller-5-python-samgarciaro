from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, color_escamas, cantidad_aletas):
        super().__init__(nombre, edad, habitat, genero)
        self.__color_escamas = color_escamas
        self.__cantidad_aletas = cantidad_aletas

    def getColorEscamas(self):
        return self.__color_escamas

    def getCantidadAletas(self):
        return self.__cantidad_aletas

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