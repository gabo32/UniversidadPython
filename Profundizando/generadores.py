# Generadores
# es una funcion especial que retorna una secuencia de valores y sustepende la eejcucio
# no se usa return

def generador():
    # producir
    yield 1
    print('Se reanuda la ejecucion')
    yield 2
    print('Se reanuda la ejecucion')
    yield 3

#consumir el generador
gen = generador()
#con cada llamada se consume un valor
print(next(gen))
print(next(gen))
print(next(gen))
#Error
#print(next(gen))


#consumir con for
for valor in generador():
    print(f'Numero producido {valor}')
