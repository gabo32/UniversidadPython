#expresion generadora es un generador anonimo
multiplicacion = (valor*valor for valor in range(4))
print(multiplicacion)
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

#pasar expresion generadora a funcion (sin parentesis)
import math
suma = sum(valor*valor for valor in range(4))
print(suma)

#expresiones generadora
