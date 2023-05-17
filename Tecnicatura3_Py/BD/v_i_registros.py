import psycopg2 #esto es para conectar con postgresql

conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido,email) VALUES (%s,%s,%s)'
            valores = (('Carlos','Lara','clara@gmail.com'),
                       ('Marcos','Canto','mcanto@gmail.com'),
                       ('Marcelo','Cuenca','mcuenca@gmail.com')) #es una tupla de tuplas
            cursor.executemany(sentencia,valores) #De esta manera ejecutamos la sentencia
            #conexion.commit() esto se utiliza para guardar los cambios en la bbdd. Con with no es necesario ponerlo ya lo hace automaticamente
            registros_insertados = cursor.rowcount #ingresar cada columna los valores
            print(f'Los registros insertados son: {registros_insertados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()