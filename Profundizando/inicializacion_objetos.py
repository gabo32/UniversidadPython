# orden de inicializacion de objetos

class Padre:
    def __init__(self):
        print('INicializador padre')

    def metodo(self):
        print('Metodo padre')


class Hijo(Padre):
    # llama init de la clase padre siempre y cuando la hija no tenga init
    def __init__(self):
        print('INicializador hijo')
        # llamamos al init del padre
        super().__init__()

    def metodo(self):
        print('Metodo sobreescrito en la clase hija')

#padre1 = Padre()
#padre1.metodo()

hijo1 =Hijo()
hijo1.metodo()