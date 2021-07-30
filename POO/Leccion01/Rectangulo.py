class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.altura * self.base


base = int(input('Introduce la base'))
altura = int(input('Introduce la altura'))

rectangulo1 = Rectangulo(base, altura)

print(f'El area del rectangulo es: {rectangulo1.calcularArea()}')
