from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, color_escamas, largo_cola):
        super().__init__(nombre, edad, habitat, genero)
        self.__color_escamas = color_escamas
        self.__largo_cola = largo_cola

    def getColorEscamas(self):
        return self.__color_escamas

    def getLargoCola(self):
        return self.__largo_cola

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil.iguanas += 1
        return cls(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes += 1
        return cls(nombre, edad, "jungla", genero, "blanco", 1)

    @classmethod
    def cantidad_reptiles(cls):
        return len(cls.listado)
