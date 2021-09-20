#leer contenido online
from urllib.request import urlopen

with urlopen( 'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:

    contenido = mensaje.read().decode('utf-8')
    print(contenido)

    palabras = []
    for linea in mensaje:
        palabras_por_line = linea.decode('utf-8').split()
        for palabra in palabras_por_line:
            palabras.append(palabra)

    print(palabras)

    #contar ocurrencias
    print(contenido.count('Universidad'))
    print(contenido.upper())
    print(contenido.lower())
    print('python'.lower() in contenido.lower())

    print(contenido.startswith('GlobalMentoring'))
    print(contenido.endswith('GlobalMentoring.com.mx'))

    mensaje = 'Hola Mundo'
    print(mensaje.islower())
    print(mensaje.lower().islower())#true
    print(mensaje.isupper())
    print(mensaje.upper().isupper())

with open('nuevo_archivo.txt','w', encoding='utf-8') as archivo:
    archivo.write(contenido)


