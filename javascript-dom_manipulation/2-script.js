const para = document.getElementById("red_header");
const cabecera = document.querySelector("header");

para.addEventListener("click", function() {
    cabecera.classList.add("red");
});
