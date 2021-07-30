# listas
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# imprimir la lista
print(nombres)
print(nombres[0])
print(nombres[1])
# acceder a elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# rangos de 0 a 2 sin incluir 2
print(nombres[0:2])
# ir del inicio de la lista al indice sin incluirlo
# desde el inicio hasta el 3
print(nombres[:3])
# desde el indice indicado hasta el final
print(nombres[1:])
# cambiar el valor de la lista
nombres[3] = 'Ivon'
print(nombres)

for nombre in nombres:
    print(nombre)
else:
    print('No hay mas nombres en la lista')

# preguntar tamanio de una lista
print(len(nombres))

nombres.append('Lorenzo')

print(nombres)

nombres.insert(1, 'Octavio')
print(nombres)

nombres.remove('Octavio')
print(nombres)

nombres.pop()
print(nombres)

# eliminar el elemento 0
del nombres[0]
print(nombres)

nombres.clear()
print(nombres)

# borrar lista por completo
del nombres
# print(nombres) # error ya no se puede acceder despues de borrarlo

rango = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in rango:
    if num % 3 == 0:
        print(num)

# tuplas no se pueden modificar si solo se tiene un valor hay que poner una coma al final
frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)
print(len(frutas))
print(frutas[2])
print(frutas[-1])
print(frutas[0:1])

for fruta in frutas:
    print(fruta, end=' ')
# error no se puede modificar
# frutas[0] = '';
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('')
print(frutas)
del frutas
#print(frutas)
print('*********************')
tupla = (13,1,8,3,2,5,8)
lista = []
for t in tupla:
    if t < 5:
        lista.append(t)
print(lista)

print('*********************')
# coleccion tipo set no guarda orden
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
print(len(planetas))
# revisar si existe un elemento
print('Marte' in planetas)
print('Martes' in planetas)
# agregar
planetas.add('Tierra')
print(planetas)
# no soporte elementos duplicados
planetas.add('Tierra')
print(planetas)
# eliminar pero arroja error si no lo encuentra
planetas.remove('Tierra')
print(planetas)
# planetas.remove('Tierras')
print(planetas)
planetas.discard('Jupiter')
print(planetas)
# no arroja error al eliminar
planetas.discard('Jupiters')
print(planetas)
planetas.clear()
print(planetas)
del planetas
print('*****************************')
# diccionarios
diccionario = {
    'IDE': 'Integrated development environment',
    'OOP': 'Object oriented programming',
    'DBMS': 'Database management system'
}
print(diccionario)
print(len(diccionario))
# acceder a elemento
print(diccionario['IDE'])
# recuperar elemento
print(diccionario.get('OOP'))
# modificar
diccionario['IDE'] = 'INTEGRATED DEVELOPMENT ENVIRONMENT'
print(diccionario)

# recorrer diccionario
for termino, valor in diccionario.items():
    print(termino, valor)
for termino in diccionario.keys():
    print(termino)
for valor in diccionario.values():
    print(valor)

# existencia de elemento
print('IDE' in diccionario)
print('IDe' in diccionario)

#agregar
diccionario['PK'] = 'Primary key'
print(diccionario)

# remover
diccionario.pop('DBMS')
print(diccionario)
diccionario.clear()
print(diccionario)
del diccionario
#print(diccionario)
