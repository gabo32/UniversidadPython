from NumerosIdenticosException import NumerosIdenticosException
resultado = None


try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))

    if a == b:
        raise NumerosIdenticosException('Numeros identicos')

    resultado = a/b
except ZeroDivisionError as zde:
    print(f'Ocurrio un error: {zde}, {type(zde)}')
except TypeError as e:
    print(f'Ocurrion un error cadena: {e}, {type(e)}')
# la mas generica al final
except Exception as e:
    print(f'Ocurreio un erorr: {e}, {type(e)}')
else:
    print('NO se lazo ninguna exception')
finally:
    print('Siempre se ejecuta')

print(f'Resultado: {resultado}')
print('continuamos...')