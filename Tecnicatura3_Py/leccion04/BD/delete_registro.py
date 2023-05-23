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
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            entrada= input('digite el umero de rgsitro a eliminar: ')
            valores =(entrada,)
            cursor.execute(sentencia,valores)#ejecutamos la sentencia
            registros_eliminados= cursor.rowcount#recuperamos solo la tupla seleccionada
            print(f'regsitros eliminados son: {registros_eliminados}')  

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()