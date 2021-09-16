console.log('Corriendo el word selector js');
// Se levanta el elemento
function handleDragStart(e) {
    this.style.opacity = '0.4';    
    e.dataTransfer.setData("word", this);
}
// Se suelta el elemento y se vuelve a poner visible
function handleDragEnd(e) {//termina el jaloneo
    this.style.opacity = '1';
}
function testSr(e) {//Elemento aceptado
    console.log('elemento alojado');
}
    
// Funciones para la caja

// Se suelta un elemento en una caja q espera
function handleDrop(e) {    
    console.log('Tevas a quedar ok');
    this.classList.remove('over');    
    let elemento = e.dataTransfer.getData('word');
    console.log(elemento);
    e.target.appendChild(elemento)
    // agregar elemento a la lista    
    return false;
}
// Se acerca a el elemento y saluda
function handleDragEnter(e) {
    console.log('Hola como estas');
    this.classList.add('over');
}
// Se aleja el elemento y se despide
function handleDragLeave(e) {
    console.log('chao q te vaya bien');
    this.classList.remove('over');
}
function handleDragOver(e) {
    e.preventDefault();
    return false;
}

let items = document.querySelectorAll('.box');
items.forEach(function (item) {
    item.addEventListener('dragenter', handleDragEnter);
    item.addEventListener('dragleave', handleDragLeave);
    item.addEventListener('dragover', handleDragOver);
    item.addEventListener('drop', handleDrop);    
});

let words = document.querySelectorAll('.word');
words.forEach(function (word) {
    word.addEventListener('dragstart', handleDragStart);
    word.addEventListener('dragend', handleDragEnd);
    word.addEventListener('drop', testSr);
    // word.addEventListener('dragenter', handleDragEnter);
    // word.addEventListener('dragleave', handleDragLeave);
});
