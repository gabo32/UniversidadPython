class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # sobre carga +
    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

# es igual
#obj1 + obj2
#obj1.__add__(obj2)
person1 = Persona('Juan', 28)
person2 = Persona('Carlos', 33)

print(person1 + person2)
print(person1 - person2)