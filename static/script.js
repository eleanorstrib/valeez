$(document).ready(function(){
	$('#get-packing').hide()

  $('#get-packing-button').on('click', function get_packing(evt) {
    alert("HEY!");
    evt.preventDefault();
    var url = "/getpacking?city=" + $('#city-field').val() + "&depart_date=" + $('#depart-date').val() + "&return_date=" + 
      $('#return-date').val() + "&trip_type=" + $('#trip-type').val() + "&gender=" + $('#gender').val() + '"';
    $('#get-packing').show();
    console.log("prevented default")
    console.log(url);
    $.get('/getpacking', function(packing){
      $('#get-packing').append(packing);
    });
    return false;
  })
});

$(function() {
    $( "#depart-date, #return-date" ).datepicker({
        defaultDate: "+1w",
        minDate: "+1d",
        maxDate: "+10d",
    
        });
  });

