from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, color_piel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.__color_piel = color_piel
        self.__venenoso = venenoso

    def getColorPiel(self):
        return self.__color_piel

    def isVenenoso(self):
        return self.__venenoso

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        Anfibio.ranas += 1
        return cls(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        Anfibio.salamandras += 1
        return cls(nombre, edad, "selva", genero, "negro y amarillo", False)

    @classmethod
    def cantidad_anfibios(cls):
        return len(cls.listado)