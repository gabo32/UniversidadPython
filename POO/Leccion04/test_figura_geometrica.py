from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(lado = 5, color = 'Rojo')
print('Creacion de cuadrado'.center(50, '-'))
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'Area: {cuadrado1.calcular_area()}')

#MRO method resolution order
# Orden en que se resuelven las llamadas a los metodos
# el orden se define por las clases padre
print(Cuadrado.mro())

print(cuadrado1)

print('Creacion de rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho= 3, alto= 8, color = 'Verde')
print(f'Calculo del area: {rectangulo1.calcular_area()}')
print(rectangulo1)
rectangulo1.alto = -10
print(rectangulo1)
rectangulo1.alto = 4
print(rectangulo1)

# No se puede instanciar porque es abstracta
# figura = FiguraGeometrica()

print(Cuadrado.mro())