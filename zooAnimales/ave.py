from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, color_plumas):
        super().__init__(nombre, edad, habitat, genero)
        self.__color_plumas = color_plumas

    def getColorPlumas(self):
        return self.__color_plumas
    
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