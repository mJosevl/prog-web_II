var nota = 9; //tipo entero
var precio = 124.99; //tipo decimal

var mensaje ="Se ha guardado el archivo satisfactoriamente";
var sexo = 'f';

var esPar = false;
var encontrado = true;

list <list> listaproducto = new ArrayList<string>();
listaproducto.add("mouse");
listaproducto.add("impresora");
listaproducto.add("plotter");
listaproducto.add("microfono");
listaproducto.add("speaker");

let nombre = null;
let apodo = "SuperCoder";
let edad = 25;
let mayorDeEdad = edad >= 18 && "Sí" && true; // Sí
let saludo = nombre || apodo || "Anónimo"; // SuperCoder
let negacion = !saludo; // false
console.log("Hola, soy " + saludo + ". ¿Soy mayor de edad? " + mayorDeEdad + ". ¿Y si niego mi saludo? " + negacion + ".");

// Este código muestra cómo se evalúan los operadores lógicos, de comparación y aritméticos en JavaScript
let a = 10;
let b = 5;
let c = 2;
let d = true;
let e = false;
let f = a + b > c * d && !e || a - b < c / d && e; // ¿Qué valor tendrá f?

let f = a + b > c * d && !e || a - b < c / d && e; // Código original
let f = 15 > 4 && !e || 5 < 1 && e; // Se evalúan las operaciones aritméticas
let f = true && !e || false && e; // Se evalúan las comparaciones
let f = true && true || false && false; // Se niega el valor de e
let f = true || false; // Se evalúa el AND
let f = true; // Se evalúa el OR
