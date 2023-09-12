/* Declarar y definir variables a utilizar */

var estadoLicuadora = "apagado";
var sonidoLicuadora = document.getElementById("licuadora-sonido");
var botonLicuadora = document.getElementById("licuadora-boton-sonido");
var licuadora = document.getElementById("licuadora");

/* Función que enciende y apaga la licuadora */

function controlarLicuadora() {
  if (estadoLicuadora == "apagado") {
    estadoLicuadora = "encendido";
    sonidoMotor();
    licuadora.classList.add("active");
  } else {
    estadoLicuadora = "apagado";
    sonidoMotor();
    licuadora.classList.remove("active");
  }
}

/* Función que maneja los sonidos del botón y el motor de la licuadora */

function sonidoMotor() {
  if (sonidoLicuadora.paused) {
    botonLicuadora.play();
    sonidoLicuadora.play();
  } else {
    botonLicuadora.play();
    sonidoLicuadora.pause();
    sonidoLicuadora.currentTime = 0; /* Reinicia el audio al segundo 0 */
  }
}