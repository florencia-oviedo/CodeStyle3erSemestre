// -- Arreglos o Arrays --

// (visualizacion mediante Quokka)
//let autos = new Array('Ferrari', 'Renault', 'BMW'); // sintaxis vieja

const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);
console.log(autos[2]);

// Recorremos el arreglo
for( let i= 0; i<autos.length; i++){
    console.log((i+1)+'- '+autos[i]);
}

// modificamos los elementos del arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

// Agregar nuevos elementos al arreglo
autos.push('Audi'); // lo agrega al final
console.log(autos);

// Otras formas de agregar elementos (usando el arreglo)
autos[autos.length] = 'Porsche';
console.log(autos);

autos[6] = 'Renault'; // Cuidado!, saltea una posicion y crea un elemento vacio. No es aconsejable usar esta forma
console.log(autos);

// ¿Como preguntar si es un array?
console.log(Array.isArray(autos)); // devuelve un bool
console.log(autos instanceof Array);