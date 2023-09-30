const item = document.getElementById("add_item");


item.addEventListener("click", function(){
    const lista = document.querySelector(".my_list");
    const nuevo = document.createElement("li");
    nuevo.textContent = "Item";
    lista.appendChild(nuevo);
});
