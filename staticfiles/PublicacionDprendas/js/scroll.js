window.addEventListener("scroll", function() {
    var nav = document.querySelector(".initial-nav");
    if (window.scrollY > 100) {
      nav.classList.add("fixed-nav");
    } else {
      nav.classList.remove("fixed-nav");
    }
  });
  