// -- Funciones en Javascript --

miFuncion(8, 2); // Esto se conoce como hosting, llamar la fn antes de definirla.

function miFuncion(a, b){
    console.log("Sumamos: "+(a+b));
}

// Llamamos a la funcion

miFuncion(5, 4);

// La palabra Return
function miFuncion2(a, b){
   return a + b ;
}
let  resultado = miFuncion2(6, 7);
console.log(resultado);

// Funciones de tipo expresion o anonima
let x = function(a, b){return a + b};
resultado2 = x(10, 8);          // se llama poniendo parentesis a la variable
console.log(resultado2);

// Funciones de tipo self e invoking
(function(a, b){
    console.log('Ejecutando la funcion: '+ (a + b));
})(9, 6);  // estos paretensisi llaman la funcion automticamente a si misma. por unica vez y no se puede retutilizar.

// Tipos de datos en una funcion

console.log(typeof miFuncion); // nos dirá que es de tipo function
function miFuncionDos(a, b){
    console.log(arguments); // nos devuelve cada posicion y valor de los argumentos
 }
miFuncionDos(5, 7);

var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto); 

// Funciones flecha  - Ecmascrpt6
const sumaFuncionFlecha = (a, b) => a + b;
resultado = sumaFuncionFlecha(10, 25); 
console.log(resultado);

// Argumentos y parametros  (diferencia)
function parametros(a , b){return a+b};     // a y b son Parametros
parametros(10, 20);                         // 10 y 20 so los argumentos

let sumar = function(a = 4, b = 12){
    console.log(arguments[0]); // muestra el argumento de a:
    console.log(arguments[1]); // muestra el argumento de b:
    console.log(arguments[2]); // muestra el 3er argumento pasado en la llamada de la fn
    return a + b;
    // return a + b + arguments[2];  // probar quietando el anterior return
}
resultado = sumar(3, 2, 9);
console.log(resultado);

// Hoisting - Se puede usar una funcion antes de haberla declarado

let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);

// sumar todos los argumentos pasados
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i <arguments.length; i++){
        suma += arguments[i];  // arguments es para arreglos
    }
    return suma;
}

// Paso por valor - cuando utilizamos tipos que no son objetos, valores primitivos

let k = 10;
function cambiarValor(a){
    a = 20;
    return a;
}

let m = cambiarValor(k); // no cambia el valor de K, envia una copia de su valor
console.log(k);
console.log(m);

// Paso por referencia - creamos un objeto con propiedades

const persona = {
    nombre: 'Martin',
    apellido: 'Verstra'
}
console.log(persona.nombre);
console.log(persona.apellido);

function cambiarValorObjeto(p1){
    p1.nombre = 'Alejandro';
    p1.apellido = 'Perez';
}
cambiarValorObjeto(persona);

console.log(persona.nombre);
console.log(persona.apellido);