$(function() {
	$( "#accordion" ).accordion();

	var availableTags = [
		"ActionScript",
		"AppleScript",
		"Asp",
		"BASIC",
		"C",
		"C++",
		"Clojure",
		"COBOL",
		"ColdFusion",
		"Erlang",
		"Fortran",
		"Groovy",
		"Haskell",
		"Java",
		"JavaScript",
		"Lisp",
		"Perl",
		"PHP",
		"Python",
		"Ruby",
		"Scala",
		"Scheme"
	];
	$( "#autocomplete" ).autocomplete({
		source: availableTags
	});

	$( "#button" ).button();
	$( "#radioset" ).buttonset();

	$( "#dialog" ).dialog({
		autoOpen: false,
		width: 400,
		buttons: [
			{
				text: "Ok",
				click: function() {
					$( this ).dialog( "close" );
				}
			},
			{
				text: "Cancel",
				click: function() {
					$( this ).dialog( "close" );
				}
			}
		]
	});

	// Link to open the dialog
	$( "#dialog-link" ).click(function( event ) {
		$( "#dialog" ).dialog( "open" );
		event.preventDefault();
	});

	$( "#datepicker" ).datepicker({
		inline: true
	});

	$( "#slider" ).slider({
		range: true,
		values: [ 17, 67 ]
	});

	$( "#progressbar" ).progressbar({
		value: 20
	});

	// Hover states on the static widgets
	$( "#dialog-link, #icons li" ).hover(
		function() {
			$( this ).addClass( "ui-state-hover" );
		},
		function() {
			$( this ).removeClass( "ui-state-hover" );
		}
	);
	// run the currently selected effect
	function runEffect() {
	  // get effect type from
	  var selectedEffect = $( "#effectTypes" ).val();
	 
	      // most effect types need no options passed by default
	  var options = {};
	  // some effects have required parameters
	  if ( selectedEffect === "scale" ) {
	    options = { percent: 0 };
	  } else if ( selectedEffect === "transfer" ) {
	    options = { to: "#button", className: "ui-effects-transfer" };
	  } else if ( selectedEffect === "size" ) {
	        options = { to: { width: 200, height: 60 } };
	      }
	 
	      // run the effect
	  $( "#effect" ).effect( selectedEffect, options, 500, callback );
	    };
	 
	    // callback function to bring a hidden box back
	function callback() {
	  setTimeout(function() {
	    $( "#effect" ).removeAttr( "style" ).hide().fadeIn();
	      }, 1000 );
	    };
	 
	    // set effect from select menu value
	$( "#button" ).click(function() {
	  runEffect();
	  return false;
	});
});
