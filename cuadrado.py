from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    '''
    Clase que representa un objeto cuadrado.
    '''

    def __init__(self, lado):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)

# Implementación del encapsulamiento con property, setter  y validaciones.
    @property
    def lado(self):
        return self._ancho

    @lado.setter
    def lado(self, new_lado):
        self.ancho = new_lado
        self.alto = new_lado

    def area(self):
        return self._ancho * self._ancho

    def perimetro(self):
        return 4 * self._ancho

    def __str__(self):
        return f"Cuadrado - Lado: {self._ancho}"