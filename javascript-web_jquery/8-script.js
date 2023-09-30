$(document).ready(function() {
    $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
      $.each(data.results, function(index, movie) {
        var title = movie.title;
        $("UL#list_movies").append("<li>" + title + "</li>");
      });
    });
  });
