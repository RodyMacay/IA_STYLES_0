document.addEventListener('DOMContentLoaded', function () {
    // Obtén una referencia al botón "Enviar Imágenes"
    const submitImagesButton = document.getElementById('submit-images');

    // Verifica que el elemento con ID 'submit-images' existe en el DOM
    if (submitImagesButton) {
        // Escucha el evento de clic en el botón "Enviar Imágenes"
        submitImagesButton.addEventListener('click', function () {
            const iaGeneratedDetails = `
                <p>Descripción: Estos zapatos son ideales para actividades deportivas y al aire libre.</p>
                <p>Tipo: Zapatos deportivos</p>
                <p>Marca: Nike</p>
                <p>Talla: 42</p>
                <p>Estado: Nuevo</p>
                <p>Precio: 28</p>
            `;

            // Botones para Atrás, Editar y Publicar
            const buttons = `
                <button id="back-button">Atrás</button>
                <button id="edit-button">Editar</button>
                <button id="publish-button">Publicar</button>
            `;

            // Actualiza el contenido del contenedor "ai-details-container"
            const aiDetailsContainer = document.getElementById('ai-details-container');
            if (aiDetailsContainer) {
                aiDetailsContainer.innerHTML = `${iaGeneratedDetails}${buttons}`;

                // Manejar eventos para los botones
                const backButton = document.getElementById('back-button');
                const editButton = document.getElementById('edit-button');
                const publishButton = document.getElementById('publish-button');

                // Agrega eventos de clic a los botones
                if (backButton) {
                    backButton.addEventListener('click', function () {
                        // Acción para el botón "Atrás"
                        // Puedes redirigir a la página anterior o realizar la acción deseada aquí
                    });
                }

                if (editButton) {
                    editButton.addEventListener('click', function () {
                        // Acción para el botón "Editar"
                        // Puedes permitir al usuario editar los detalles aquí
                    });
                }

                if (publishButton) {
                    publishButton.addEventListener('click', function () {
                        // Acción para el botón "Publicar"
                        // Puedes realizar la acción de publicación aquí
                    });
                }
            }
        });
    }
});