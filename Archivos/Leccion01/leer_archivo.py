try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    #print(archivo.read())

    #leer algunos caracteres
    # print(archivo.read(5))
    # print(archivo.read(3))

    #leer lineas completas
    #print(archivo.readline())
    #print(archivo.readline())

    #iterar archivo
    #for linea in archivo:
    #    print(linea)

    #todas las lineas
    #print(archivo.readlines())

    #una linea
    #print(archivo.readlines()[2])

    #copiar un archivo a otro
    archivo2 = open('copia.txt', 'w', encoding='utf8')
    archivo2.write(archivo.read())


except Exception as e:
    print(e)