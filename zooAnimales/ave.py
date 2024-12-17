from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    listado = []

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_plumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.__color_plumas = color_plumas
        Ave.listado.append(self)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones += 1
        return cls(nombre, edad, "montañas", genero, "café glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave.aguilas += 1
        return cls(nombre, edad, "montañas", genero, "blanco y amarillo")

    @classmethod
    def cantidad_aves(cls):
        return len(cls.listado)