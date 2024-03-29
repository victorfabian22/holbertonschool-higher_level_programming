const list_movies = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        movies.forEach(movie => {
            const li = document.createElement("li");
            li.textContent= movie.title;
            list_movies.appendChild(li);
        });
    })
    .catch(error => {
        console.log("Error", error);
    });
