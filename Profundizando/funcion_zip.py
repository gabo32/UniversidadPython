# mostrar funciones builtins
# print(dir(__builtins__))
# help(zip)

numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
identificadores = 321, 322, 323, 324, 325
conjunto = {6, 4, 0, 9, 8, 15, 10}
# lista de tuplas
mezcla = zip(numeros, letras, identificadores, conjunto)
print(mezcla)
print(list(mezcla))
# mezcla = zip(numeros, letras)
# print(tuple(mezcla))


# iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Numero: {numero}, letra: {letra}, id: {id}, aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')

print(nueva_lista)

# unzip
mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*mezcla)
print(f'Numeros: {numeros}, letras: {letras}')

# ordenar un zip
letras = ['c', 'd', 'a', 'b']
numeros = [3, 2, 4, 1, 0]
mezcla = zip(letras, numeros)
print(tuple(mezcla))
print(sorted(zip(numeros, letras)))

# diccionario con zip y 2 iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

#actualizar diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)

