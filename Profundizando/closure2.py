def operacion(a, b):
    # definir lambda interna
    return lambda: a + b

print(operacion(4,5)())