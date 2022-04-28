class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    #métodos
    def agregarZonas(self, zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            total += len(zona.cantidadAnimales())
        return total
    
    #getters & setters
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

