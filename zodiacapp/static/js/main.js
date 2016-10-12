$(document).ready(function(){
  console.log("main.js ready!");
});

$( "#zodiac_form_id" ).submit(function( event ) {
  console.log( "Handler for .submit() called." );

  var year = parseInt($('#yyyy').val());
  var month = parseInt($('#mm').val());
  var day = parseInt($('#dd').val());

  // date checker
  if (dateChecker(year, month, day) == false) {
    return false;
  }

  $.ajax({
    type: "POST",
    url: "/api/",
    data: {year: year, month: month, day: day},
    success: function(results){
      console.log(results);
      display_result(results.data);

      $('#yyyy').val('');
      $('#mm').val('');
      $('#dd').val('');
    },
    error: function(error) {
      console.log(error);
    }
  });

  event.preventDefault();
});

function display_result(data) {
  $('#result').show()

  $('#westImage').attr('src', data.westZodiac.imageurl);
  $('#westImage').attr('width', 300);
  $('#westImage').attr('height', 300);

  $('#eastImage').attr('src', data.eastZodiac.imageurl);
  $('#eastImage').attr('width', 300);
  $('#eastImage').attr('height', 300);

  $('#westCaption').html(data.westZodiac.name)
  $('#eastCaption').html(data.eastZodiac.name)
}

function dateChecker(year, month, day) {
  if (year < 0 || year > 9999) {
      alert("We can't calculate people who were born before A.C. or after 9999");
      return false;
  };
  if (month < 1 || month > 12) {
      alert("From scale 1 - 12, your month is out of range");
      return false;
  };

  dayInMonth = new Date(year, month, 0).getDate();

  if (day < 0 || day > dayInMonth){
      alert("day from 1 - " + dayInMonth);
      return false;
  };
  return true;
}
