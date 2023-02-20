// JQUERY Select and Manipulate a header using 'click'

$('DIV#add_item').on('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});
