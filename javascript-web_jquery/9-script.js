$(document).ready(function() {
    $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
      var translation = data.hello;
      $("#hello").text(translation);
    });
  });
