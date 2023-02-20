// JQUERY to fetch and load an object from an API in the background, then manipulate DOM to display the info

$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
  });
});
