const menuIcons = document.querySelectorAll('.menu-icon');

menuIcons.forEach((icon) => {
  icon.addEventListener('click', (event) => {
    event.stopPropagation();
    const options = icon.querySelector('.options');
    options.style.display = options.style.display === 'block' ? 'none' : 'block';
  });
});

// Cierra el menú si se hace clic en cualquier parte de la página
document.addEventListener('click', () => {
  menuIcons.forEach((icon) => {
    const options = icon.querySelector('.options');
    options.style.display = 'none';
  });
});
