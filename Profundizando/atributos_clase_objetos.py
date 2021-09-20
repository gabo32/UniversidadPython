class Persona:
    constador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


#mostrar attributos de objeto
persona1 = Persona('Juan', "Perez")
print(persona1.__dict__)

# Crear atributos al vuelo
print(persona1.constador_personas)

# no se puede modficar desde el objeto
persona1.contador_personas = 10
print(persona1.__dict__)

# acceder a variable de clase
print(Persona.constador_personas)

# segundo objeto
persona2 = Persona('Karla', 'Gomez')
print(persona2.__dict__)

#atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)