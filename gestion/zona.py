class Zona:
     def __init__(self, nombre, zoologico=None):
        self.__nombre = nombre
        # Si no se pasa un zoológico, se establece un valor predeterminado
        self.__zoologico = zoologico if zoologico else None

    def agregar_animales(self, animal):
        self.__animales.append(animal)
        animal.set_zona(self)

    def cantidad_animales(self):
        return len(self.__animales)

    def getNombre(self):
        return self.__nombre

    def getZoologico(self):
        return self.__zoologico

