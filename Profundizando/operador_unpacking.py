# * desempaquetar
numeros = [1, 2, 3]
print(numeros)
print(*numeros, sep=' - ')


def sumar(a, b, c):
    print(f'Resultado de la suma: {a + b + c}')


# utilizando unpacking
sumar(*numeros)

# Extraer algunas partes de una lista
mi_lista = [1, 2, 3, 4, 5, 6]
a, *b, c,d = mi_lista
print(a,b,c,d)

# unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(lista3)
lista3 = [*lista1, *lista2]
print(lista3)

# unir diccionarios
dic1 = {'A':1, 'b':2, 'c':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(dic3)

#lista a partir de str
lista = [*'HOla mundo']
print(lista)
print(*lista, sep='')