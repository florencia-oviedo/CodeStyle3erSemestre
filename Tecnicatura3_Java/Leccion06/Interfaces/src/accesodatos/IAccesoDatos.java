
package accesodatos;


public interface IAccesoDatos {
    
    int MAX_REGISTROS=10;
    
    //metodo insertar abstracto y sin cuerpo
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
    
}
