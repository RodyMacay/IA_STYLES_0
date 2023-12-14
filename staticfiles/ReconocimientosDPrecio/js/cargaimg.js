document.addEventListener('DOMContentLoaded', function () {
  // Obtén una referencia al elemento de entrada de carga de imágenes
  const imageUploadInput = document.getElementById('image-upload');

  // Verifica que el elemento con ID 'image-upload' existe en el DOM
  if (imageUploadInput) {
    // Obtén una referencia al contenedor de imágenes seleccionadas
    const selectedImagesContainer = document.getElementById('selected-images-container');

    // Escucha el evento de cambio en el elemento de entrada de carga de imágenes
    imageUploadInput.addEventListener('change', function () {
      // Borra cualquier imagen previamente mostrada
      selectedImagesContainer.innerHTML = '';

      // Recorre las imágenes seleccionadas y muéstralas
      for (const file of imageUploadInput.files) {
        const imageElement = document.createElement('img');
        imageElement.src = URL.createObjectURL(file);
        imageElement.classList.add('selected-image');
        selectedImagesContainer.appendChild(imageElement);
      }
    });
  }})