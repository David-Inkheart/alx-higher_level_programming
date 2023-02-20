// jQuery used to manipulate the DOM in response to user events.

$(document).ready(function () {
  // add item
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  // remove item
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last-child').remove();
  });

  // clear list
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
