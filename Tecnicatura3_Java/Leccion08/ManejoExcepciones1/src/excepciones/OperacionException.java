
package excepciones;


public class OperacionException extends RuntimeException{
    //Constructor
    public OperacionException(String mensaje){
        super (mensaje);
    }
}
