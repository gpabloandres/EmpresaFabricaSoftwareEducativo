// Desplazamiento suave al hacer clic en los enlaces de navegación
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const targetId = this.getAttribute("href");
    document.querySelector(targetId).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// Botones para volver al inicio al final de cada sección
document.querySelectorAll(".back-to-top").forEach((button) => {
  button.addEventListener("click", function (e) {
    e.preventDefault();

    document.querySelector("header").scrollIntoView({
      behavior: "smooth",
    });
  });
});

// Animación simple al botón de llamado a la acción
const ctaButton = document.querySelector(".cta-button");

ctaButton.addEventListener("mouseenter", function () {
  ctaButton.style.backgroundColor = "#FF8C5A";
});

ctaButton.addEventListener("mouseleave", function () {
  ctaButton.style.backgroundColor = "#FF5733";
});
