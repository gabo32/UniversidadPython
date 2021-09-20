import psycopg2

# conexion a postgres
conexion = psycopg2.connect(user='postgres', password='juan1323.,', host='localhost', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            # valores = ('jUAN cARLOS', 'Juarez', 'jcclara@mail.com', 1)
            valores = (('Juan ', 'Perez', 'jcclara@mail.com', 1),
                       ('Ivonne', 'GUtierrez', 'igutierrez@mail.com', 2))
            #cursor.execute(sentencia, valores)
            cursor.executemany(sentencia, valores)

            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
