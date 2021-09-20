# Todas la clases heredan de object
class Persona(object):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo to string
    def __str__(self):
        return f'Persona: {self.nombre} {self.edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'


empleado1 = Empleado('Juan', 28, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
