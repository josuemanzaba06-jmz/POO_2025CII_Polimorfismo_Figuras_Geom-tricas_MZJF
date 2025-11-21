'''
Programa principal para mostrar el uso de figuras geométricas
'''
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia

# Crear dos cuadrados
cuadrado1 = Cuadrado(5)
cuadrado2 = Cuadrado(8)

# Crear dos rectángulos
rectangulo1 = Rectangulo(4, 6)
rectangulo2 = Rectangulo(10, 3)

# Crear dos circunferencias
circunferencia1 = Circunferencia(3)
circunferencia2 = Circunferencia(5)

# Mostrar las figuras
print(f"Cuadrado 1: {cuadrado1}")
print(f"Area: {cuadrado1.area()}")
print(f"Perimetro: {cuadrado1.perimetro()}")
print()

print(f"Cuadrado 2: {cuadrado2}")
print(f"Area: {cuadrado2.area()}")
print(f"Perimetro: {cuadrado2.perimetro()}")
print()

print(f"Rectangulo 1: {rectangulo1}")
print(f"Area: {rectangulo1.area()}")
print(f"Perimetro: {rectangulo1.perimetro()}")
print()

print(f"Rectangulo 2: {rectangulo2}")
print(f"Area: {rectangulo2.area()}")
print(f"Perimetro: {rectangulo2.perimetro()}")
print()

print(f"Circunferencia 1: {circunferencia1}")
print(f"Area: {circunferencia1.area()}")
print(f"Perimetro: {circunferencia1.perimetro()}")
print()

print(f"circunferencia 2: {circunferencia2}")
print(f"Area: {circunferencia2.area()}")
print(f"Perimetro: {circunferencia2.perimetro()}")
print()

# Modificar valores
print("--- Modificando valores ---")
cuadrado1.lado = 10
print(cuadrado1)
print(f"Nueva area: {cuadrado1.area()}")
print()

rectangulo1.ancho = 7
rectangulo1.alto = 12
print(rectangulo1)
print(f"Nueva area: {rectangulo1.area()}")
print()

circunferencia1.radio = 7
print(circunferencia1)
print(f"Nueva area: {circunferencia1.area()}")
print()

# Probar valores inválidos (Validación)
print("--- Probando valores invalidos ---")
print("Intentando crear cuadrado con lado -5:")
cuadrado_malo = Cuadrado(-5)
print()

print("Intentando cambiar ancho del rectangulo a -3:")
rectangulo1.ancho = -3
print()

print("Intentando cambiar alto del rectangulo a 0:")
rectangulo1.alto = 0
print()


# Crear lista de figuras
figuras_geo = list()
figuras_geo = [cuadrado1, cuadrado2, rectangulo1, rectangulo2, circunferencia1, circunferencia2]

# Funcion para sumar areas implementando polimorfismo
def sumar_areas(figuras):
    total = 0
    for figura in figuras:
        total = total + figura.area()
    return total

# Funcion para sumar perimetros implementando polimorfismo
def sumar_perimetros(figuras):
    total = 0
    for figura in figuras:
        total = total + figura.perimetro()
    return total

print("--- Suma de Areas y Perimetros ---")
print(f"Total de areas: {sumar_areas(figuras_geo)}")
print(f"Total de perimetros: {sumar_perimetros(figuras_geo)}")