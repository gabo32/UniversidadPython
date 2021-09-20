import psycopg2 as db

conexion = db.connect(user='postgres', password='juan1323.,', host='localhost', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s,%s)'
            valores = ('Alex', 'Rojas','mesparza@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = ('Juan Perexz', 'Perez', 'mail.@mail.com', 4)
            cursor.execute(sentencia, valores)
except Exception as e:
    print(f'Ocurrio un error:, se hizo rollback {e}')
finally:
    conexion.close()
print('Termina la transaccion, se hizo commit')
