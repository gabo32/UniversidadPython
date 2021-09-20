class Clase1:
    def __init__(self):
        print('CLase1.__init__')

    def metodo(self):
        print('Clase1.metodo')


class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Clase2.metodo')
        super().metodo()


class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('CLase3.metodo')
        super().metodo()


class Clase4(Clase2, Clase3):
    def metodo(self):
        print('Clase4.metodo')
        super().metodo()


#creamos objeto clase4
clase4 = Clase4()
print(Clase4.__bases__)
print(Clase4.__mro__)

clase4.metodo()