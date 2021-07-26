print("Hola mundo con Python")

# Variables
miVariable = 'Hola desde python'
print(miVariable)

# el tipo de variables es dinamico
miVariable = 2
print(miVariable)

# operaciones
x = 10
y = 2
z = x + y
print(x)
print(y)
print(z)

# imprimir direcciones de memoria
print(id(x))
print(id(y))
print(id(z))

# Tipos de datos
print("Tipos de datos: ")
x = 10
# mostrar el tipo de variable
print(x)
print(type(x))
x = 'Hola Mundo'
print(x)
print(type(x))
# se puede indicar el tipo de dato pero no es obligatorio
x: str = 'Hola mundo string'
print(x)
print(type(x))
# Entero
x = 11
print(x)
print(type(x))
# Flotante
x = 10.5
print(x)
print(type(x))
# Boolean
x = True
print(x)
print(type(x))
x = False
print(x)


# Cadenas
miGrupoFavorito = "Metallica"
comentario = "The Best Rock Band"
print("Mi grupo favorito es: " + miGrupoFavorito + " " + comentario)
# uso de comas, le añade un espacio entre las cadenas
print("Mi grupo favorito es:", miGrupoFavorito, comentario)

numero1 = "1"
numero2 = "2"
# concatenacion
print( "Concatenacion", numero1 + numero2)
# suma con strings
# convertir a entero
int(numero1)
int(numero2)
print("Suma: ", int(numero1) + int(numero2))

numero1 = 1
numero2 = 2
print("Suma de enteros", numero1 + numero2)

print("Booleanos: ")
miVariable = False
print(miVariable)

miVariable = 1 > 2
print(miVariable)

if miVariable:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")


print("Entrada de usuario")
# FUncion input
numero1 = input("Escribe el primer numero: ")
numero2 = input("Escrie el seguno numerp")

resultado = int(numero1) + int(numero2)

print("El resultado es: ", resultado)

print("Como estuvo tu dia:")
resultado = input("Introduce del 1 al 10")
print("Mi dia estuvo de:", resultado)

print("Fin del programa")