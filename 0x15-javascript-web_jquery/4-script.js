// JQUERY Select and Manipulate a header using 'click'

$('DIV#toggle_header').on('click', function () {
  $('header').toggleClass('green');
  $('header').addClass('red');
});
