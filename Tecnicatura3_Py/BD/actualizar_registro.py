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
            sentencia = 'UPDATE persona SET nombre=%s , apellido=%s , email=%s WHERE id_persona= %s'
            valores = ('Juan Carlos','Roldan','rcarlos@gmail.com', 1)
            cursor.execute(sentencia,valores) #De esta manera ejecutamos la sentencia
            registros_actualizados = cursor.rowcount #ingresar cada columna los valores
            print(f'Los registros actualizados son: {registros_actualizados }')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()