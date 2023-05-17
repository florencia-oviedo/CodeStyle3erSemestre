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
            #sentencia='SELECT * FROM persona'
            #sentencia='SELECT id_persona, nombre FROM persona'
            #sentencia='SELECT * FROM persona WHERE id_persona=1'
            sentencia='SELECT * FROM persona WHERE id_persona = %s' #PLACEHOLDER
            id_persona=input('digite un numero para el id_persona: ')
            #cursor.execute(sentencia)#ejecutamos la sentencia
            cursor.execute(sentencia,(id_persona,))#ejecutamos la sentencia
            #registros= cursor.fetchall()#recuperamos todos los registros que serán una lista
            registros= cursor.fetchone()#recuperamos solo la tupla seleccionada
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html