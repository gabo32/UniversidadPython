# permiten transformar de manera rogramatica una clase, similar a decoradores de clase (metaprogramacion)
import inspect


def decorador_repr(cls):
    print('1. Se ejecuta decorador')
    print(f'REcibos el objeto de la clase: {cls.__name__}')

    # revisamos los atributros de la clase el con emetodo vars
    atributos = vars(cls)
    # for nombre, atributo in atributos.items():
    #    print(nombre, atributo)
    # revisamos si se ha escrito init
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito __init__')

    firma_init = inspect.signature(cls.__init__)
    print('Fiorma init', firma_init)
    # recuperamos parametros sin self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros init {parametros_init}')

    # revisar si cada parametro tiene un properti asociado
    for parametro in parametros_init:
        es_metrodo_property = isinstance(atributos.get(parametro), property)
        if not es_metrodo_property:
            raise TypeError(f'No existe un metodo properti para el parametro {parametro}')
    return cls


@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self.apellido

    # def __repr__(self):
    #    return f'Persona({self._nombre}, {self._apellido})'


persona1 = Persona('Juan', 'Gab')
