import psycopg2
conexion= psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
);
try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia='UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores= (
                ('Juan Jose', 'Rojas','rojas@mail.com', 1),('Jose Jose', 'Joss','jjj@mail.com',2)
                )# es una tupla de tuplas
            cursor.executemany(sentencia,valores)#ejecutamos la sentencia
            registros_actualizados= cursor.rowcount#recuperamos solo la tupla seleccionada
            print(f'los registros actualizados son: {registros_actualizados}')  

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()