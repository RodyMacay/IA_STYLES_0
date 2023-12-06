document.addEventListener("DOMContentLoaded", function () {
    // Obtener el elemento de mensajes
    var messagesContainer = document.getElementById('messages-container');

    // Aplicar estilos
    if (messagesContainer) {
        messagesContainer.style.color = '#721c24';
        messagesContainer.style.border = '1px solid #f5c6cb';
        messagesContainer.style.padding = '10px';
        messagesContainer.style.margin = '10px 0';
        messagesContainer.style.borderRadius = '5px'; // Agregar esquinas redondeadas
    }

    // Ocultar el mensaje después de 2 segundos
    setTimeout(function() {
        if (messagesContainer) {
            messagesContainer.style.display = 'none';
        }
    }, 2000);
});
