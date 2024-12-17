from zooAnimales.Animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    listado = []

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_escamas=None, largo_cola=None):
        super().__init__(nombre, edad, habitat, genero)
        self.__color_escamas = color_escamas
        self.__largo_cola = largo_cola
        Reptil.listado.append(self)

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
