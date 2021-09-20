import psycopg2

# conexion a postgres
conexion = psycopg2.connect(user='postgres', password='juan1323.,', host='localhost', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN  %s'
            # llaves_primarias = ((1,2,3,4),)

            entrada = input('Proporciona los ids a buscar: (separado por ,)')
            llaves_primarias = (tuple( entrada.split(',')),)
            # id_persona = input('Proporciona el valor de id_persona: ')
            # hay que convertirlo a tupla
            #cursor.execute(sentencia, (id_persona,))
            cursor.execute(sentencia, llaves_primarias)
            # recupera todos
            registros = cursor.fetchall()
            # recupera uno
            # registros = cursor.fetchone()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
