# REpresentacion de objetos (str, repr, format)
# print(dir(object))

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # repr mas enfocado a programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido: {self.apellido})'
        # return f'{self.__class__.__name__}{self.__dict__}'

    # str esta mas enfocado al usuario final u otros sistemas
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    #su implementacion por defecto es str
    #se llama cuando se imprimr un fstring
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Juan', 'Perez')
print(persona1)
# asegura el llamado a repr
print(f'Mi objecto persona1: {persona1!r}')
print(persona1)
#format
print(f'{persona1}')