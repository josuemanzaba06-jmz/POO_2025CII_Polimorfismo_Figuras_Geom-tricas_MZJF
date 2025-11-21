class FiguraGeometrica:
    '''
    SuperClase, base para representar figuras geométricas
    '''

    def __init__(self, ancho, alto):
        self._ancho = None
        self._alto = None
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, new_ancho):
        # Validación para Anchura
        if new_ancho > 0:
            self._ancho = new_ancho
        else:
            print("Error: El ancho debe ser mayor que 0")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, new_alto):
        # Validación para Altura
        if new_alto > 0:
            self._alto = new_alto
        else:
            print("Error: El alto debe ser mayor que 0")

    def area(self):
        return self._ancho * self._alto

    def perimetro(self):
        pass

    def __str__(self):
        return f"Figura Geometrica - Ancho: {self._ancho}, Alto: {self._alto}"