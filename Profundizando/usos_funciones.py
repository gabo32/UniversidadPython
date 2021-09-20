# las funciones en python con ciudadanas de primera clase
# first class citizens

# definimos la funcion
def sumar(a, b):
    return a + b


# asignar funcion a variable
mi_funcion = sumar

# verificar el tipo de la variable
print(type(mi_funcion))
resultado = mi_funcion(3, 5)
print(resultado)


# funcion como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado de sumar: {sumar(a, b)}')


operacion(4, 5, sumar)


# retornar funcion
def retornar_function():
    return sumar

mi_funcion_retornada = retornar_function()
print(f'Resultado de funcionr etornada: {mi_funcion_retornada(5,7)}')
