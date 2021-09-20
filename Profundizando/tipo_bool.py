#TIpos numericos 0 es False, >0 es true

valor = 0
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')


valor = 15.0
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')

#tipo str False para ''

valor = ''
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')

#colecciones False colecciones vacias
valor = []
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')

valor = [1,2,4]
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')

#tupla
valor = ()
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')

valor = (2,3,5)
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')

#diccionamrio
valor = {}
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')

valor = {'nombre':'Juan', 'apellido':"perez"}
resultado = bool(valor)
print(f'REsultado: {valor} {resultado}')


if bool(0):
    print('Verdadero')
else:
    print('false')