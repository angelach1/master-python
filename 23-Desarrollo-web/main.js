//alert('hola mundo!!');

var nombre = "Ángel Alhambra";
var altura = 190;

var concatenacion = nombre + " " + altura;
//document.write(concatenacion);

var datos = document.getElementById("datos");

datos.innerHTML = concatenacion;

datos.innerHTML = `
   <h1>Soy la caja de datos </h1>
   <h2>Mi nombre es: ${nombre}</h2>
   <h3>Mido: ${altura} cm</h3>
`;

if (altura >= 190) {
   datos.innerHTML += "<h1>Eres una persona ALTA</h1>";
} else {
   datos.innerHTML += "<h1>Eres una persona BAJITA</h1>";
}

for (var i = 2015; i <= 2020; i++) {
   // blque de instrucciones
   datos.innerHTML += "<h2>Estamos en el año: " + i;
}

function MuestraMiNombre(nombre, altura) {
   var datos = document.getElementById("datos");
   datos.innerHTML += `
      <h1>Soy la caja de datos que se ejecuta llamando a la función MuestraMiNombre</h1>
      <h2>Mi nombre es: ${nombre}</h2>
      <h3>Mido: ${altura} cm</h3>
   `;
}

MuestraMiNombre("Ángel Alhambra Web 111", 168);

var nombres = ["Ángel", ["Antonio"], ["Joaquín"]];

document.write("<h2>Listado de nombres</h2>");

/*for (i = 0; i < nombres.length; i++) {
   document.write(nombres[i] + "<br/>");
}*/

nombres.forEach(function(nombre){
   document.write(nombre + "<br/>");
});

document.write("<h2>Listado de nombres</h2>");

nombres.forEach((nombre) => {
   document.write(nombre + "<br/>");
});

