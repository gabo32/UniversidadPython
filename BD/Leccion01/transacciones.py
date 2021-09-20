import psycopg2 as db

# conexion a postgres
conexion = db.connect(user='postgres', password='juan1323.,', host='localhost', port='5432', database='test_db')

try:
    # valor por defecto en false, es mala practica
    # conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s,%s)'
    valores = ('Carlos', 'Lara','mesparza@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan Carglos', 'Gabriel', 'mail.@mail.com', 4)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print('Termina la transaccion, se hizo commit')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error:, se hizo rollback {e}')
finally:
    conexion.close()
