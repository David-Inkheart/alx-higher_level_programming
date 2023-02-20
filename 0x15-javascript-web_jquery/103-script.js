// fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/';
  $('#btn_translate, #language_code').click(() => {
    const languageCode = $('#language_code').val();
    $.get(`${apiUrl}?lang=${languageCode}`, (data) => {
      $('#hello').html(data.hello);
    });
  });
});
