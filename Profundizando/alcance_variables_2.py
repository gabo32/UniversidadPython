# mas de funciones anidadas y alcance de variables

def funcion_externa():
    variable_local_externa = 'Variable local externa'

    def function_anidada():
        variable_local_anidada = 'Variable local anidada'

        #trabajar con la variable de fuera
        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor variable local externa'


    function_anidada()
    print(f'Valor variable local externa: {variable_local_externa}')

funcion_externa()