class Persona:

    # constructor
    # __dunder
    def __init__(self, nombre, apellido, edad):
        # atributos de instancia
        # _ indica que este atributo no se deberia acceder desde fuera
        # __ indica que no se puede modificar
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # getter
    # decorador
    @property
    def nombre(self):
        return self._nombre

    # setter
    # si se quita el set se dice que es una variable de solo lectura
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad


    @edad.setter
    def edad(self, edad):
        self._edad = edad


    # hay que agregar self a todos los metodos de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} edad: {self._edad}')

    # metodo destructor
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)

    # no se debe hacer
    persona1._nombre = 'Juan Gabriel'
    # no se puede moficiar
    persona1.__nombre = 'Juan Jose'
    persona1.mostrar_detalle()

    # se llama al metodo nombre
    print(persona1.nombre)
    # se llama al setter
    persona1.nombre = 'Juan jj'
    print(persona1.nombre)
    persona1.apellido = 'SMith'
    persona1.edad = 33
    persona1.mostrar_detalle()

    #nombre del modulo
    print(__name__)