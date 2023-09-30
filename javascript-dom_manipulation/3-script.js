const toggle = document.getElementById("toggle_header");
const header = document.querySelector("header");

toggle.addEventListener("click", function(){
    if (header.classList.contains("red")) {
        header.className = "green";
    }
    else {
        header.className = "red";
    }
});
