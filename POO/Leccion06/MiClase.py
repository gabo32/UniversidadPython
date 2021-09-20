class MiClase:

    # variable estatica
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # metodos estaticos
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # emtodos de clase cls es la clase
    @classmethod
    def metodo_clase(cls):
         print(cls.variable_clase)

print(MiClase.variable_clase)
miClase = MiClase('valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

miClase2 = MiClase('otro valor de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_instancia)

#variables al vuelo
MiClase.variable_clase2 = 'Valor variable clase 2'

print(MiClase.variable_clase2)
print('***')
# llamar metodo estatico
MiClase.metodo_estatico()

#llamar metodo de clase
MiClase.metodo_clase()

miObjecto1 = MiClase('Variable instancia')
# un objeto si puede acceder al contexto estatico
miObjecto1.metodo_clase()
miObjecto1.metodo_estatico()`