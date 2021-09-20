# alcance de variables

var_global = 'Variable global'


def imprimir():
    # indicamos que se trabajar con variable global
    global var_global
    # acceder a variable globarl
    print(f'Variable global desde funcion: {var_global}')
    # variable local
    var_local = 'Variables local'
    print(f'Variable local desde funcion: {var_local}')
    var_global = 'Nuevo valor' # error

    def function_anidada():
        print(f'Variable local dentro de funcion anidada: {var_local}')

    function_anidada()

imprimir()
print(f'Variable globar fuera de fucnion: {var_global}')
# print(f'Variable local: {var_local}')
