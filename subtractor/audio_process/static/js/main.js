// A $( document ).ready() block.
$( document ).ready(function() {

	$.get( "/media/Ghosts_echoed_RIR_noise_testfile_SUBTRACTED.wav", function( r, text_status ) {
	console.log(text_status);
	console.log('testing');
    // response = r;
	});


	// $.ajax({ cache: false,
	//   url: "/Admin/Contents/GetData",
	//   data: { accountID: AccountID },
	//   success: function (data) {
	//   $('#CityID').html(data);
	//   },
	//   error: function (ajaxContext) {
	//   alert(ajaxContext.responseText)
	//   }
	// });

    // console.log( "ready!" );
});

