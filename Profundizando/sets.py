# set es una coleccion de elementos univos
# los elementos deben ser inmutables ( una lista no)
conjunto = {'juan', True, 19, 0}
print(conjunto)

# set vacio
conjunto = {}  # este es un diccionario
print(type(conjunto))

# set vacio
conjunto = set()
print(conjunto)
print(type(conjunto))

conjunto.add('juan')
print(conjunto)

# valores unicos
conjunto.add('juan')
print(conjunto)

# crear un set a partir de iteralbl
conjunto = set([4, 5, 6, 7, 4])
print(conjunto)

# agrega mas elementos o set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20, 30, 40, 40])
print(conjunto)

# copia poco profunda
conjunto_copoia = conjunto.copy()
print(conjunto_copoia)
print(f'Es igual en contenido {conjunto == conjunto_copoia}')
print(f'Es igual en referncia {conjunto is conjunto_copoia}')

# operaciones de conjuntos
pelo_negro = {'Juan', 'Karla', "Pedro", 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}

# Todos con ojos cafe y pelo rubio (union)
print(ojos_cafe.union(pelo_rubio))
print(pelo_rubio.union(ojos_cafe))

# interseccion personas con ojos cafe y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))

# difference pelo negro sin ojos cafes
print(pelo_negro.difference(ojos_cafe))

#diferencia asimetrica quitar los comunes pelo negro u ojos cafes
print(pelo_negro.symmetric_difference(ojos_cafe))


#operaciones con conjuntos
#preguntar si un set esta dentro de otro
print(menores_30.issubset(pelo_negro))

#super set
print(menores_30.issuperset(pelo_negro))

#nada en comun
print(pelo_negro.isdisjoint(pelo_rubio))