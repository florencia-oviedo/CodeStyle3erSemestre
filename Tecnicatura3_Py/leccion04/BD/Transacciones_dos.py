import psycopg2 as bd # Esto es para poder conectarnos a Posgre

conexion = bd.connect(user='postres', password='admin', host='127.0.0.01', port='5432', database='test.bd')
try:
    conexion.automcommit = False # Esto directamente no debería estar, inicia la transacción
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Carlos','Lara', 'clara@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan', 'Juarez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit() # HAcemos el commit manualmente, se cierra la transacción
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()
