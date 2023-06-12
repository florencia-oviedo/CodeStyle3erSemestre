'''
 ---  Transacciones: ejecucion de varias consultas en una BD que modifican datos, de manera exitosa con with.  ---
'''
import psycopg2 as bd # para importar la libreria de Postgre

# -- Configuracion de la conexion --
conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
#print(conexion) #para comprobar si se conectó
# con with
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Jimena', 'Cardoso', 'cardojim@gmail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores =('Rosa', 'Roldan', 'roldanro@gmail.com', 11)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrió un error se hizo un rollback: {e}')
finally:
    conexion.close()

print('Termina la transaccion')