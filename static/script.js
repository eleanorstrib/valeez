 // $(document).ready(function(){
 // 	$('#get-packing').hide()
 // });


  $(function() {
    $( "#depart-date, #return-date" ).datepicker({
        defaultDate: "+1w",
        minDate: "+1d",
        maxDate: "+10d",
    
        });
  });