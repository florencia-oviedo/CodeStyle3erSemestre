//let persona3 = new Persona("Carla", "Ponce");
// no se puede crear un objeto antes de que esté la clase creada
class Persona{  //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

}

class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        this._departamento;
    }

    set departamento(departamento){
        this.departamento = departamento;
    }
}

let persona1 = new Persona("Martin", "Perez");
console.log(persona1.nombre);
console.log(persona1.apellido);
persona1.nombre = "Juan Carlos";
console.log(persona1.nombre)
persona1.apellido = "López";
console.log(persona1.apellido)
//console.log(persona1);
let persona2 = new Persona("Carlos", "Lara");
console.log(persona2.nombre);
console.log(persona2.apellido);
persona2.nombre = "María Laura";
console.log(persona2.nombre);
persona2.apellido = "González";
console.log(persona2.apellido);
//console.log(persona2);


let empleado1 = new Empleado("María", "Giménez", "Sistemas");
console.log(empleado1);

