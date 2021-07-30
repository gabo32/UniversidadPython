def miFuncion(nombre, apellido):
    print('Saludos desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}')


miFuncion('Juan', 'Perez')
miFuncion('Karla', 'Lara')


# indica que puede regresar un int pero no es obligatorio
def sumar(a: int = 0, b: int = 0) -> int:
    return a + b


resulta = sumar(1, 4)
print(f'Resultado de la suma {resulta}')
print(f'Resultado de la suma {sumar(1, 4)}')

# valores por defecto
print(sumar())


# argumento variables se convierte a tupla
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')


def sumaTodo(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total


print(sumaTodo(1, 2, 3, 4, 5, 6, 7, 8, 9))


def multiplicaTodo(*numeros):
    total = 1
    for num in numeros:
        total *= num
    return total


print(multiplicaTodo(3, 4, 5))


# recibir llave valor
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')


listarTerminos(IDE='Integrate deveopment environment', PK='Primary key')
listarTerminos(DBMS='Database management system')


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((10, 11))
desplegarNombres([10, 11])

print()


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(900))
print('**')


def imprimir(num):
    print(num)
    if num > 1:
        imprimir(num - 1)


print(imprimir(5))
