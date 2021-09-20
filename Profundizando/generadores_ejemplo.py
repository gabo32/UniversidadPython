#generador de numeros del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecucion')



generador = generador_numeros()
print(f'Obujeto generador {generador}')
print(type(generador))
for valor in generador:
    print(valor)


generador = generador_numeros()
try:
    print(f'Consumismos {next(generador)}')
    print(f'Consumismos {next(generador)}')
    print(f'Consumismos {next(generador)}')
    print(f'Consumismos {next(generador)}')
    print(f'Consumismos {next(generador)}')
    print(f'Consumismos {next(generador)}')
    print(f'Consumismos {next(generador)}')
except StopIteration as e:
    print(f'Error en el consumirodr {e}')


generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'IMpresion del valor {valor}')
    except StopIteration as e:
        print('Termino la iteracion del generador')
        break
