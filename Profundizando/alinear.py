titulo = 'Sitio web de globalmentoring.com.mx'
print(len(titulo))
print(titulo.center(50, '*'))
print(titulo.center(len(titulo)+10, '-'))

#alinear a la izquierda
print(titulo.ljust(50, '*'))

print(titulo.rjust(50, '-'))

#replace
print('hola mundo'.replace(' ','-'))

titulo = '   ****    Globalmentoing.com.mx   ***    '
print(titulo)
titulo = titulo.strip()
print(titulo)
titulo = titulo.strip('*')
print(titulo)
titulo = '****    Globalmentoing.com.mx   ***'.lstrip('*')
print(titulo)
titulo = '****    Globalmentoing.com.mx   ***'.rstrip('*')
print(titulo)

titulo = '   ****    Globalmentoing.com.mx   ***    '.strip().strip('*').strip()
print(titulo)