class Persona:

    # constructor
    # __dunder
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        # atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    # hay que agregar self a todos los metodos de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} edad: {self.edad} {self.valores} {self.terminos}')
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    # indica que ya no se pondra nada mas
    # indicar que cree la clase pero sin contenido
    pass


# crear objeto persona
persona1 = Persona('Juan', 'Perez', 28)

print(type(Persona))
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona1.nombre = 'Juan Gabriel'
persona1.apellido = 'Juarez'
persona1.edad = 25

print(f'Objecto persona: {persona1.nombre} {persona1.apellido} edad: {persona1.edad}')

persona2 = Persona('Karla', 'Gomez', 30)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

persona1.mostrar_detalle()
persona2.mostrar_detalle()

Persona.mostrar_detalle(persona1)

# agregar atributo al objeto
persona1.telefono = '1234556'
print(persona1.telefono)
# la persona 2 no tiene el telefono
# print(persona2.telefono)
persona3 = Persona('Juan', 'Perez', 28, '55434', 2,456,6, m = 'Manzana', p='Pera')
persona3.mostrar_detalle()
