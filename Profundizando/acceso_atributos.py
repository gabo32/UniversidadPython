# ejemplo atributos publicos, protegidos y privados

class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        # protegido con el guion bajo solo la clase o subclases
        self._protegido = protegido
        # atributos privador __ solo esta clase los debe usar
        self.__privado = privado


obj = MiClase('publico', 'protegido', 'privado')
print(obj.publico)
obj.publico = 'Nuevo valor publico'
print(obj.publico)

# acceso a valor protegido
print(obj._protegido)  # mala practica
obj.protegiro = 'Nuevo valor protegido mala practica'
print(obj._protegido)

# valor privado
# print(obj.__privado) # error no se puede utilizar
# se convierte a objeto._clase__atributo privado
print(obj._MiClase__privado)  # mala practica
# modificar el valor
obj._MiClase__privado = 'Nuevo valor privador'  # mala practica en python
print(obj._MiClase__privado)  # mala practica
