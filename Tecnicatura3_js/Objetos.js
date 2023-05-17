//  -- OBJETOS EN JS --

let x = 10; // variable de tipo primitiva
console.log(x.length); // no se encontramos propiedades ni metosdos asociados -> undefined

let persona = {
  // creacion de un objeto
  nombre: "Carlos",
  apellido: "Moyano",
  email: "Carlosmoyano@gmail.com",
  edad: 28,
  idioma: "es",
  get lang() {
    return this.idioma.toUpperCase(); //Comvierte las minusculas a mayusculas
  },
  set lang(lang) {
    this.idioma = lang.toLowerCase();
  },
  nombreCompleto: function () {
    // (*1)
    return this.nombre + " " + this.apellido;
  },
  get nombreEdad() {
    //Este es el método get
    return "El nombre es: " + this.nombre + " , edad: " + this.edad;
  },
};

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);

// agregar metodo en objetos -> concatenar nombre y apelido para devolver (*1)
console.log(persona.nombreCompleto());

// Creamos un nuevo objeto de otra manera y asignamos atributos

let persona2 = new Object(); // crea un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "1123456789";

console.log(persona2.telefono);
console.log(persona["apellido"]); // Accedemos como si fuera un arreglo (para usar en ciclo FOR IN)

// como recorrer un objeto con For in
for (propiedad in persona) {
  console.log(propiedad);
  console.log(persona[propiedad]);
}

// agregar y eliminar propiedades de un objeto

console.log(persona.apellido);
persona.apellido = "Verstraeten"; // cambio dinamico de un valor del objeto
console.log(persona.apellido);

// tener cuidado de no equivocarnos al poner el atributo que deseamos cambiar porque puede generarse otro distinto. ej:
persona.nombrA = "Martin";
console.log(persona.nombre);
console.log(persona.nombrA); // -> es un nuevo atributo
// lo eliminamos...
delete persona.nombrA;

// Distintas formas de imprimir un objeto

// 1) la mas sencilla
console.log(persona.nombre + ", " + persona.apellido);

// 2) a traves de un ciclo for in
for (nombrePropiedad in persona) {
  console.log(persona[nombrePropiedad]);
}

// 3) con el Metodo Objet.values. Devuelve un arreglo
let personaArray = Object.values(persona); // nuestro objeto
console.log(personaArray);

// 4) con Json
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el metodo get  y set para idioma");
persona.lang = "en";
console.log(persona.lang);

function Persona3(nombre, apellido, email) {
  //constructor
  this.nombre = nombre;
  this.apellido = apellido;
  this.email = email;
  this.nombreCompleto = function () {
    return this.nombre + "  " + this.apellido;
  };
}
let padre = new Persona3("Leo", "Lopez", "lopezl@gmail.com");
padre.nombre = " Luis"; // modificamos el nombre
console.log(padre);
console.log(padre.nombreCompleto()); // Utilizamos la funcion
let madre = new Persona3("Laura", "Contrera", "contreral@gmail.com");
console.log(madre);
console.log(madre.nombreCompleto());
