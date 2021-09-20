# profundizando en listas son mutables

nombres1 = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura Maria Gonzalo Ernesto'.split()

# sumar listas
print(f'Suma de listas{nombres1 + nombres2}')

# extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Estender {nombres1 + nombres2}')

# lista de numeros
numeros1 = [10, 40, 5, 4, 20, 90, 4]
# obtener el indice del primer elemento
print(f'Indice 4: {numeros1.index(4)}')
print(f'Lista {numeros1}')

# invertir orden de lista
numeros1.reverse()
print(f'Lista invertida {numeros1}')

# ordenar
numeros1.sort()
print(f'Lista ordenada {numeros1}')

numeros1.sort(reverse=True)
print(f'Lista ordenada descente{numeros1}')

# obtener minimo y maxino
print(f'Minimo {min(numeros1)}')
print(f'Maximo {max(numeros1)}')

# copiar lista no profunda
numero2 = numeros1.copy()

print(numero2)
print(f'MIsma referencia? {numeros1 is numero2}')
print(f'Mismo contanido {numeros1 == numero2}')

# constructor de lista
numero2 = list(numeros1)
print(f'MIsma referencia? {numeros1 is numero2}')
print(f'Mismo contanido {numeros1 == numero2}')

# copiar slicing
numero2 = numeros1[:]
print(f'MIsma referencia? {numeros1 is numero2}')
print(f'Mismo contanido {numeros1 == numero2}')

# multiplicacion de listas
lista_multiplicacion = 5 * [[2, 5]]
print(lista_multiplicacion)
print(f'MIsma referencia? {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contanido {lista_multiplicacion[0] == lista_multiplicacion[1]}')

lista_multiplicacion[2].append(10)
print(lista_multiplicacion)

# matrices en python
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 80]]
print(matriz)
print(f'Renglon 0-, columna 0 {matriz[0][0]}')
print(f'Renglon 2, columna2 {matriz[2][2]}')
matriz[2][0] = 65
print(matriz)

lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
lista_listas.sort(key=len)
print(lista_listas)

# built in
nombres1 = ['juan carlos', 'karla', 'pedro', 'esperanza']
nombres1 = sorted(nombres1)
print(nombres1)
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)

nombres1 = sorted(nombres1, key=len)
print(nombres1)

nombres1 = reversed(nombres1)
print(list(nombres1))

