# multiplicacion de cadenas
resultado = 5 * 'Hola'
print(f'Resultado: {resultado}')

# multiplicacion de tuplas
resultado = 5 * ('HOla', 10)
print(f'Resultado: {resultado}')

# multiplicacion de listas (lista de 10 elementos con 0)
resultado = 10 * [0]
print(f'Resultado: {resultado}, largo {len(resultado)}')

# caracteres de escape
resultado = 'Hola \'mundo\''
print(f'Resultado {resultado}')

# eliminar el espacio
resultado = 'SE va a eliminar el punto.\b'
print(resultado)

resultado = 'c:\\directorio\\juan'
print(resultado)

# row string
resultado = r'Cadena con \n salto de linea'
print(resultado)

# unicode y ascii
# unicode
print('Hola\u0020Mundo')
print('NOtacion simple: ', '\u0041')
print('Notacion extendida: ', '\U00000041')
print('Notacion hexadecimal: ', '\x41')

print('Corazon: ', '\u2665')
print('Cara sonriendo: ','\U0001f600')
print('serpiente: ','\U0001f40d')


#ascii
caracter = chr(65)
print(caracter)

caracter = chr(64)
print(caracter)

caracter = chr(97)
print(caracter)


#caracteres con bytes
catacteres_en_bytes = b'Hola Mundo'
print(catacteres_en_bytes)
mensaje = b'Universiad python'
print(mensaje[0])
print(chr(mensaje[0]))

lista_catacteres = mensaje.split()
print(lista_catacteres)

string = 'Programación con python'
print('string original: ', string)
bytes = string.encode('UTF-8')
print('bytes codificados', bytes)
# convertir de bytes a strin
string2 = bytes.decode('UTF-8')
print('String 2: ', string2)