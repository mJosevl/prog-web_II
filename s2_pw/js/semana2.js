// semana2.js

// Función para obtener la fecha actual en formato legible
function obtenerFechaActual() {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date().toLocaleDateString('es-ES', options);
}

// Función para actualizar la fecha en el cuadro de diálogo
function actualizarFecha() {
    const fechaActualizacion = document.getElementById('fechaActualizacion');
    fechaActualizacion.textContent = `La página fue actualizada el ${obtenerFechaActual()}.`;
}

// Evento que se dispara al abrir el cuadro de diálogo
$('#exampleModal').on('show.bs.modal', function (e) {
    actualizarFecha();
});
