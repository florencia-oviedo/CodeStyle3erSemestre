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
            #sentencia='SELECT * FROM persona WHERE id_persona IN(1,2)' #PLACEHOLDER
            #id_persona=input('digite un numero para el id_persona: ')
            sentencia='SELECT * FROM persona WHERE id_persona IN %s' #PLACEHOLDER
            entrada = input('Digite los Id persona a buscar (separados por coma): ')
            llaves_primarias =(tuple(entrada.split(',')),)
            cursor.execute(sentencia,llaves_primarias)#ejecutamos la sentencia
            registros= cursor.fetchall()#recuperamos solo la tupla seleccionada
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()