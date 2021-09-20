# los diccionarios guardan un orden

diccionario = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 28}
print(diccionario)

# son mutables
# diccionario = {[1,2]:'valor'}

# tupla si se puede usar
#diccionario = {(1, 2): 'valor'}
#print(diccionario)

# se agrega si no existe
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# no hay llaves duplicadas
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

#recuperar info
print(diccionario['Nombre'])

# si no encuentra la lalve lanza exception
#print(diccionario['nombre'])

#metodo get pero no lanza exception, tambien devuelve un valor por defecto
print(diccionario.get('Nombre', 'No se encontro la llave'))
print(diccionario.get('Nombres', 'No se encontro la llave'))

#setdefault si modifica el diccionario en caso de no encontrar la llave y permite valor por defecto
nombre = diccionario.setdefault('Nombres', 'Valor por defecto')
print(nombre)
print(diccionario)

#imprimir diccionario
from pprint import pprint as pp
pp(diccionario, sort_dicts=False)