nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
print(mensaje_con_formato)

persona = ('Karla', 'Gomez', 5000.00)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.5f'%persona
print(mensaje_con_formato)

mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.5f'
print(mensaje_con_formato % persona)

print('*****************')
# placeholder
sueldo = 3000
mensaje = 'Nombre {}, Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Nombre {0}, Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Sueldo {2:.2f} Nombre {0}, Edad {1} '.format(nombre, edad, sueldo)
print(mensaje)


#argumentos
mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n = nombre, e = edad, s = sueldo)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'Nombre {persona[nombre]} Edad: {persona[edad]} Sueldo: {persona[sueldo]:.2f}'.format(persona=diccionario)
print(mensaje)

mensaje = f'Nombre {nombre} Edad {edad} sueldo {sueldo:.2f}'
print(mensaje)

print(nombre, edad, sueldo, sep=', ')