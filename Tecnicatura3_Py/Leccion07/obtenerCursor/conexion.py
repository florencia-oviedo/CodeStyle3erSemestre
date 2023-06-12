#Agregar método obtener cursor y Corregir errores de identación
@classmethod
def obtenerCursor(cls):
    if cls._cursor is None:
        try:
            cls._cursor = cls.obtenerConexion().cursor()
            log.debug(f'Se abrió correctmente el cursor: {cls._cursor}')
            return cls._cursur
        except Exception as e:
            log.error(f'Ocurrió un error: {e}')
            sys.exit()
    else:
        return cls._cursor
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()


