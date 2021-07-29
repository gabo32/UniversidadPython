condicion = True

while condicion:
    print('Ejecutando ciclo while')
    condicion = False
else:
    print('Se imprime cuando el ciclo while es false')

contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print('Fin del ciclo while')

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
else:
    print('FIn ciclo while')

contador = 5
while contador > 0:
    print(contador)
    contador -= 1


print('*****************************************')
cadena = 'Hola'
for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')

for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada {letra}')
        # rompe el for
        break
else:
    print('Fin ciclo for')


for i in range(6):
    if i % 2 == 0:
        print(f'Valor {i}')
    else:
        continue

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor {i}')