$(document).ready(function(){
	$('#get-packing').hide()
});


  $(function() {
    $( "#depart-date, #return-date" ).datepicker({
        defaultDate: "+1w",
        minDate: "+1d",
        maxDate: "+10d",
    
        });
  });

$('#get-packing-button').on('click', function get_packing(evt) {
  evt.preventDefault();
  console.log("prevented default")
  $.get('/getpacking', function(packing){
    $('#get-packing').append(packing);
  });
})
