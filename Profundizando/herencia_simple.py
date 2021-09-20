# ejemplo de lista simple

class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r}'


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # ordenamos los elementos
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        self.ordenar()


class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # una vez validos los elementos se agregan
        super().__init__(elementos)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero {elemento}')

    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)


class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass


lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)

lista_ordenada = ListaOrdenada([4, 3, 6, 9, 10, -1])
print(lista_ordenada)
lista_ordenada.agregar(2)
print(lista_ordenada)
print(lista_ordenada.__len__())


lista_enteros = ListaEnteros([ 1,2,3])
print(lista_enteros)


lista_enteros_ordenada = ListaEnterosOrdenada([4,5,-1,10,14,-4,])
print(lista_enteros_ordenada)

lista_enteros_ordenada.agregar(6)
print(lista_enteros_ordenada)

print(ListaEnterosOrdenada.__bases__)
print(ListaEnterosOrdenada.__mro__)


#isinstance
print(f'Es entero: { isinstance(9, int)}')
print(f'Es cadena: ', isinstance('hola', str))
print(f'Es lista de : ', isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))
print(f'Es lista de : ', isinstance(lista_enteros_ordenada, ListaEnteros))
print(f'Es lista de : ', isinstance(lista_enteros_ordenada, ListaOrdenada))
print(f'Es lista de : ', isinstance(lista_enteros_ordenada, ListaSimple))
print(f'Es lista de : ', isinstance(lista_enteros_ordenada, object))

#cualquiera de estas clases
print('es de varios tipos', isinstance(lista_enteros_ordenada, (ListaEnteros, ListaSimple)))