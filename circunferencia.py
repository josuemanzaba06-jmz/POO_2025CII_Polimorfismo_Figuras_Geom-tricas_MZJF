from figura_geometrica import FiguraGeometrica

class Circunferencia(FiguraGeometrica):
    '''
    Clase que representa un objeto circunferencia
    '''

    def __init__(self, radio):
        FiguraGeometrica.__init__(self, ancho=radio, alto=radio)

# Implementación del encapsulamiento con property, setter
    @property
    def radio(self):
        return self._ancho

    @radio.setter
    def radio(self, new_radio):
        self.ancho = new_radio
        self.alto = new_radio

    def area(self):
        return 3.1416 * self._ancho * self._ancho

    def perimetro(self):
        return 2 * 3.1416 * self._ancho

    def __str__(self):
        return f"Circunferencia - Radio: {self._ancho}"