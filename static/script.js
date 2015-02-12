$(document).ready(function{
	var minDate = $( ".selector" ).datepicker( "option", "minDate" );
	var maxDate = $( ".selector" ).datepicker( "option", "maxDate" );
	$( ".selector" ).datepicker({ minDate: "+0d" });
    $( ".selector" ).datepicker({ maxDate: "+10d" });




});