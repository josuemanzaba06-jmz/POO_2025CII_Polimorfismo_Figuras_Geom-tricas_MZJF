from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    '''
    Clase que representa un objeto rectángulo
    '''

    def __init__(self, ancho, alto):
        FiguraGeometrica.__init__(self, ancho=ancho, alto=alto)


    def area(self):
        return self._ancho * self._alto

    def perimetro(self):
        return 2 * (self._ancho + self._alto)

    def __str__(self):
        return f"Rectangulo - Ancho: {self._ancho}, Alto: {self._alto}"