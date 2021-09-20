# unpacking
valores = 1, 2, 3
print(valores)

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

# el segundo se asigna al _
valor1, _, valor3 = 1, 2, 3

print(valor1, valor3)

# asignar todos los valores a 3
valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)

valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)


def regresa_varios_datos():
    return 1, 2, 3


valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *_ = regresa_varios_datos()
print(valor1)

valor1, *valores_restantes = regresa_varios_datos()
print(valor1, valores_restantes)


hora, separador, minutos = '17:20'.partition(':')
print(hora, minutos)


