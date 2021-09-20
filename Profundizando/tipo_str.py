from mi_clase import MiClase
#concatenar
#no se pueden concatenar variables
mensaje = 'Hola'  'Mundo'
mensaje += 'universiad ''python'
print(mensaje)

#ayuda de python
help(str.capitalize)

help(MiClase)
help(MiClase.mi_metodo)
help(MiClase.__doc__)
help(MiClase.__init__.__doc__)


print('*****************************')
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()

print(f'Mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
print(f'Mensaje2: {mensaje2}, Id: {hex(id(mensaje2))}')
mensaje1 += 'adios'
print(f'Mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')


print('*****************************')
tupla_str = ('Hola','Mundo','Universidad', 'Python')
mensaje = ' '.join(tupla_str)
print(mensaje)

lista_cursos = ['java','python','angular','spring']
mensaje = ','.join(lista_cursos)
print(mensaje)

cadena = 'holaMundo'
mensaje = '.'.join(cadena)
print(mensaje)

diccionario = {'nombre':'Juan', 'apellido': 'Perez', 'edad':'18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}')
print(f'Valores: {valores}')
print('*****************************')

cursos = 'Java Python javascript angular spring Excel'

lista_cursos = cursos.split()
print(f'Lista cursor {lista_cursos}')

cursos_separados_coma = 'Java, Python, javascript, angular, spring, excel'
lista_cursos = cursos_separados_coma.split(', ',2)
print(f'Lista cursos {lista_cursos}')
