condicion = 'hola'

if condicion == True:
    print('Condicion verdadera')
elif condicion == False:
    print('COndicion falsa')
else:
    print('Condicion no reconocida')

print('****************')
numero = int(input('Proporciona un valor entre 1 y 3: '))

numeroTexto = ''
if numero == 1:
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    numeroTexto = 'Valor fuera de rango'
print(f'Numero proporcionado: {numero}- {numeroTexto}')
print('****************')
# operador ternario
print('Condicion Verdadera') if condicion else print('Condicion falsa')

print('****************')
mes = int(input('Proporciona mes del año (1 - 12)'))
# indica que esta variable no tiene ningun valor (null)
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Valor incorrecto'
print(f'Para el mes {mes} la estacion es: {estacion}')

print('****************')
edad = int(input('Proporciona tu edad'))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es bella'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios'
elif 20 <= edad < 30:
    mensaje = 'Epoca de trabajar'
else:
    mensaje = 'Estapa de vida no reconocida'

print(f'La edad es {mensaje}')