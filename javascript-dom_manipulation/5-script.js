const elemento = document.getElementById("update_header");
const header = document.querySelector("header");


elemento.addEventListener("click", function(){
    header.textContent = "New Header!!!";
});
