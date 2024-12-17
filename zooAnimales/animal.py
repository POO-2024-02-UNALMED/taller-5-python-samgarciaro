class Animal:
    totalAnimales = 0
    def __init__(self,nombre,edad,habitat,genero):
        self.__nombre=nombre
        self.__edad=edad
        self.__habitat=habitat
        self.__genero=genero
        self.__zona=None
        Animal.totalAnimales += 1

   

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getHabitat(self):
        return self.__habitat

    def getGenero(self):
        return self.__genero


    def setEdad(self, edad):
        self.__edad = edad

    def movimiento(self):
        return "desplazarse"

    def __str__(self):
        if self.__zona:
            return (f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y "
                    f"mi género es {self.__genero}, la zona en la que me ubico es {self.__zona.get_nombre()}, "
                    f"en el {self.__zona.get_zoo().get_nombre()}.")
        return f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi género es {self.__genero}."

    @classmethod
    def total_por_tipo(cls):
        return (f"Mamíferos: {Mamifero.cantidad_mamiferos()}, Aves: {Ave.cantidad_aves()}, Reptiles: {Reptil.cantidad_reptiles()}, "
                f"Peces: {Pez.cantidad_peces()}, Anfibios: {Anfibio.cantidad_anfibios()}")