from zooAnimales.animal import Animal


class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    # métodos
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1
        return halcon

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.aguilas += 1
        return aguila

    # getters & setters
    def getColorPlumas(self):
        return self._colorPlumas

    def setcolorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
