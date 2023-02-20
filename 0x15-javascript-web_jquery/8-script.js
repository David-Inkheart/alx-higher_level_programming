// JQUERY to fetch and load an object from an API in the background, then manipulate DOM to display the info

$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (index, movie) {
      $('ul#list_movies').append($('<li></li>').text(movie.title));
    });
  });
});
