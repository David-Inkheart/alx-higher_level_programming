// JQUERY using a proxy server to bypass CORS

$(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
  $.get(proxyUrl + url, function (data) {
    $('#hello').text(data.hello);
  });
});
