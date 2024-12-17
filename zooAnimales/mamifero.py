from zooAnimales.animal import Animal


class Mamifero(Animal):
    caballos = 0
    leones = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.__pelaje = pelaje
        self.__patas = patas

    def isPelaje(self):
        return self.__pelaje

    def getPatas(self):
        return self.__patas

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.caballos += 1
        return cls(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Mamifero.leones += 1
        return cls(nombre, edad, "selva", genero, True, 4)

    @classmethod
    def cantidad_mamiferos(cls):
        return len(cls.listado)
