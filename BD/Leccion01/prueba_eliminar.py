import psycopg2

# conexion a postgres
conexion = psycopg2.connect(user='postgres', password='juan1323.,', host='localhost', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona in %s'
            entrada = input('Propirciona los id_persona a eliminar')
            valores = ( tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)

            registros_insertados = cursor.rowcount
            print(f'Registros eliminados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
