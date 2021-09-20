import psycopg2

# conexion a postgres
conexion = psycopg2.connect(user='postgres', password='juan1323.,', host='localhost', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES ( %s,%s,%s)'
            valores = (('angel', 'quintana', 'clara@mail.com'),
                       ('Marcos', 'Cantu', 'clara@mail.com'),
                       ('maria', 'gonzales', 'clara@mail.com'))
            # cursor.execute(sentencia, valores)
            # insertar varios
            cursor.executemany(sentencia, valores)
            # se hace automatico
            # cursor.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
