operandoA = 3
operandoB = 2

# suma
suma = operandoA + operandoB
# interpolacion
print(f'Resultado suma: {suma}')

# Resta
resta = operandoA - operandoB
print(f'Resultado resta: {resta}')

# multiplicacion
multiplicacion = operandoA * operandoB
print(f'Resultado multiplicacion: {multiplicacion}')

# division
division = operandoA / operandoB
print(f'Resultado division: {division}')
division = operandoA // operandoB
print(f'DIvision parte entera {division}')

# modulo
modulo = operandoA % operandoB
print(f'Resultado del residuo: {modulo}')

# exponente
exponente = operandoA ** operandoB
print(f'Resultrado exponente: {exponente}')


# operadores de asignacion
miVariable = 10
print(miVariable)

# operadores de reasignacion
miVariable += 1
print(miVariable)
miVariable -= 2
print(miVariable)
miVariable *= 3
print(miVariable)
miVariable /= 2
print(miVariable)

# operador de comparacion
a = 4
b = 2

# igual
resultado = a == b
print(f'Resultado ==: {resultado}')

resultado = a != b
print(f'Resultado !=: {resultado}')

resultado = a > b
print(f'Resultado >: {resultado}')

resultado = a < b
print(f'Resultado <: {resultado}')

resultado = a <= b
print(f'Resultado <=: {resultado}')

resultado = a >= b
print(f'Resultado >=: {resultado}')


print("**************************************")
a = int(input('Escribe un valor numerico:'))

if a % 2 == 0:
    print(f'{a} es un numero par')
else:
    print(f'{a} No es un numero par')

print("*******************************************")
edadAdulto = 18
edadPersona = int(input("Proporciona tu edad: "))

if edadPersona >= edadAdulto:
    print(f'La persona es un adulto')
else:
    print(f'La persona es menor de edad')

print("*******************************************")
# operadores logicos
a = True
b = False
resultado = a and b
print(resultado)
resultado = a or b
print(resultado)
a = not a
print(a)
print("*******************************************")
valor = int(input('Proporciona un numero: '))
valorMinimo = 0
valorMaximo = 5

dentroDelRango = valor >= valorMinimo and valor <= valorMaximo
if dentroDelRango:
    print(f'{valor} Esta dentro del rango')
else:
    print(f'{valor} No esta dentro del rago')

print("*******************************************")
vacaciones = False
diaDeDescanso = False

if vacaciones or diaDeDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene deberes que hacer')

if not (vacaciones or diaDeDescanso):
    print('No puede ver el partido')
else:
    print('Si puede ver el partido')
print("*******************************************")

edad = int(input('INtroduce tu edad'))

veites = edad >= 20 and edad < 30
print(veites)
treintas = edad >= 30 and edad < 40
print(treintas)

if veites or treintas:
    # print('Estas en los veintes y treintas')
    if veites:
        print('Dentro de los 20\'s')
    elif treintas:
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango')
else:
    print('No estas en los veintes ni treintas')
print("*******************************************")
print("Proporcione los siguientes datos del libro: ")
nombre = input('Proporciona el nombre del libro: ')
id = int(input('Proporciona el ID del libro: '))
precio = float(input('Proporciona el valor del libro: '))
envioGratuito = input('Indica si es envio gratuito: (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe escribir True o False'
# imprimir en varias lineas con formato
print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envio Gratuito?: {envioGratuito}
''')
