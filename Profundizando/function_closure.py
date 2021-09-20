# closure es una funcion que define a otra y ademas la regrsa

#funcion principal
def operacion(a, b):
    #definimos una funcion interna anidada
    def sumar():
        return a+b

    # retornar la funcion
    return sumar

mi_funcion_closure = operacion(5,3)
print(f'Mi funcion closure {mi_funcion_closure()}')

# llamar al vuelo
print(operacion(2,3)())