// Detectar el evento de scroll
window.addEventListener("scroll", function() {
  var nav = document.querySelector(".initial-nav");
  var scrollToTop = document.querySelector(".scroll-to-top");

  if (window.scrollY > 100) {
    nav.classList.add("fixed"); // Agregamos la clase "fixed" para hacer fijo el nav
    scrollToTop.style.opacity = 1;
  } else {
    nav.classList.remove("fixed"); // Removemos la clase "fixed" para hacerlo relativo
    scrollToTop.style.opacity = 0;
  }
});

// Agregar un evento de clic para desplazarse hacia arriba cuando se hace clic en la flecha
document.querySelector(".scroll-to-top").addEventListener("click", function() {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});
