const URL = "https://hellosalut.stefanbohacek.dev/?lang=fr";


document.addEventListener("DOMContentLoaded", function(){
    fetch(URL)
    .then(response => response.json())
    .then(data => {
        const d = document.getElementById("hello");
        d.textContent = data.hello;
    }).catch(error => {
        console.error("Error fetching translation:", error);
      });
});
