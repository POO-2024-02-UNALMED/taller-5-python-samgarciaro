class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    listado = []

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_piel=None, venenoso=None):
        super().__init__(nombre, edad, habitat, genero)
        self.__color_piel = color_piel
        self.__venenoso = venenoso
        Anfibio.listado.append(self)

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