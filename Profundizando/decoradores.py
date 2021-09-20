#Decoradores es una funcion que recibe una funcion y regresa otra y se utiliza para extender funcionalidad
# 1. Funcion decorador (a)
# 2. Funciona a decorar (b)
# 3 Fucnion decorada (c)
#El decorador debe ejecutar la funcion que recibe
def funcion_decorador_a(funcion_a_decorar_b):
    def function_decorada_c(*args, **kwargs):
        print('ANtes de ejecutar la funcion ')
        funcion_a_decorar_b(*args, **kwargs)
        print('Despues de ejcutar la funcion')

    return function_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print('HOla desde funcion mostrar mensaje')


mostrar_mensaje()


@funcion_decorador_a
def imprimir():
    print('Hola desde imprimir')


print()
imprimir()



