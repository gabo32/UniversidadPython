# Funciones anidadas

def calculadora(a, b, operacion='sumar'):
    # funcion anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # llamadas a funcion anidada
    if operacion == 'sumar':
        print(f'Suma: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Restar: {restar(a, b)}')


calculadora(5, 6, operacion='restar')
