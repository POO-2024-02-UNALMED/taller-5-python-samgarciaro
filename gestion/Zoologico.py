class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__zonas = []

    def agregar_zonas(self, zona):
        self.__zonas.append(zona)

    def cantidad_total_animales(self):
        return sum(zona.cantidad_animales() for zona in self.__zonas)

    def get_nombre(self):
        return self.__nombre
