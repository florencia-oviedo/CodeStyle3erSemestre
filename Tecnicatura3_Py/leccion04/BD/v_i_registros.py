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
            sentencia='INSERT INTO persona(nombre, apellido, email)VALUES(%s,%s,%s)' #PLACEHOLDER
            valores= (('Martin','Lara','clara@email.com'),('Marcos','Cesto','otr@mail.com'))# es una tupla
            cursor.executemany(sentencia,valores)#ejecutamos la sentencia
            #conexion.commit()# esto se utiliza para guardar cambios en la BD
            registros_insertados= cursor.rowcount#recuperamos solo la tupla seleccionada
            print(f'los registros insertados son: {registros_insertados}')
          

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()