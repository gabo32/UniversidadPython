class Cubo:

    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundidad = profundo
        self.alto = alto

    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundidad


ancho = int(input('Introduce el ancho'))
alto = int(input('Introduce el alto'))
produndidad = int(input('Introduce la profundidad'))

cubo1 = Cubo(ancho,produndidad, alto)
print(f'El volumen del cubo es: {cubo1.calcularVolumen()}')