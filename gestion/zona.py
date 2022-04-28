class Zona:
    def __init__(self, nombre):
        self._nombre = nombre
        self._zoo = []
        self._animales = []

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre

    def getZoo(self):
        return self._zoo

    def getAnimales(self):
        return self._animales
