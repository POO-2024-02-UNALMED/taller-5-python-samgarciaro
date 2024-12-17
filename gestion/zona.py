class Zona:
    def __init__(self, nombre, zoo):
        self.__nombre = nombre
        self.__zoo = zoo
        self.__animales = []

    def agregar_animales(self, animal):
        self.__animales.append(animal)
        animal.set_zona(self)

    def cantidad_animales(self):
        return len(self.__animales)

    def getNombre(self):
        return self.__nombre

    def getZoologico(self):
        return self.__zoologico

