# funciones lambda son funciones anonimas y pequeñas

# no se puede
#mi_variable =  def sumar(a, b):return a + b

# funcion lambda de una sola linea de codigo
mi_funcion_lambda = lambda a, b: a+b

print(mi_funcion_lambda(3,5))

# Funcdion lambda sin argumentos
mi_funcion_lambda = lambda : 'Funcion sin argumentos'
print(mi_funcion_lambda())

# parametros por default
mi_funcion_lambda = lambda  a =  2, b=3: a+b

print(f'Funcion con default', mi_funcion_lambda())
print(f'Funcion con default', mi_funcion_lambda(3,4))

#funcion lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)

print(f'fSuma : {mi_funcion_lambda(1,23,a=5, b=6)}')

mi_funcion_lambda = lambda a,b,c =3, *args, **kwargs: a +b+c+ len(args) + len(kwargs)
print(f'Resultados function lambda {mi_funcion_lambda(1,2,4,5,6,7,e=6,f=7)}')