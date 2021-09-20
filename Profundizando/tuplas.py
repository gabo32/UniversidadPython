#las tuplas son inmutables

#declarar variables
a, b, = 'HOla', 'adios'
print(a, b)

#swap
a, b = b,a
print(a, b)

#regresdar multiples valores
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax([1,2,3,4,5])
print(f'MInimo: {min},maximo: { max}')

#regresar suma de una tupla
resultado = sum((1,2,3,4,5))
print(resultado)

def sumar(*args):
    return sum(args)

resultado = sumar(1,2,3,4,5)
print(resultado)