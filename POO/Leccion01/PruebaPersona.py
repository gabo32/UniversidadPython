# importar del archivo Persona la clase persona
from Persona import Persona

print('Creacion de objecto'.center(50,'-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminando objetos'.center(50,'-'))
del persona1