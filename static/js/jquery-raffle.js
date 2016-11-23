		// When document loads, initialize the interface.
		$(
			function(){
				var jForm = $( "form:first" );
				var jSelect = jForm.find( ":input[ name = 'count' ]" );

				// Populate the select box.
				for (intI = 1 ; intI <= 100 ; intI++){

					// Add select option.
					jSelect.append( "<option value=\"" + intI + "\">" + intI + "</option>" );

				}


				// Hook up raffle button.
				jForm.submit(
					function( objEvent ){
						// Run raffle.
						RunRaffle( participants );

						// Prevent default.
						return( false );
					}
					);
			}
			);


		// Initializes and runs the raffle.
		function RunRaffle( intCount ){
			var jRaffle = $( "#raffle" );

			// Clear the raffle list.
			jRaffle.empty();

			// Create a new list item for each lot.
			for (var intI = 1 ; intI <= intCount ; intI++){

				// Create the lot item.
				jRaffle.append( "<li><div>" + intI + "</div></li>" );

			}

			// Find the "on" element.
			var jCurrentLI = jRaffle.find( "li:first" ).addClass( "on" );

			// Get base pause time.
			var intPause = 40;

			// Get the time to wait before chaning the pause time.
			var intDelay = (4500 + (Math.random() * 2000));


			// Define the ticker.
			var Ticker = function(){

				var jNextLI = jCurrentLI.next( "li" );

				// Check to see if there is a next LI.
				if (!jNextLI.length){

					// Since there is no LI left in the list, our next LI will be the
					// first one in the list.
					jNextLI = jRaffle.find( "li:first" );

				}

				// Turn off the current list.
				jCurrentLI.removeClass( "on" );

				// Turn on next list.
				jNextLI.addClass( "on" );

				// Store the new LI in the current LI (for next iteration).
				jCurrentLI = jNextLI;


				// Check to see if we should start changing the pause duration.
				if (intDelay > 0){

					// Substract from the delay.
					intDelay -= intPause;

				} else {

					// Change the pause.
					intPause *= (1 + (Math.random() * .1));

				}

				// Check to see how long the pause it. Once it gets over a certain wait
				// time, we are done playing and picking the winner.
				if (intPause >= 400){

					// We found a winner!
					winner = jCurrentLI.text();
					swal({   title: "Tenemos un ganador: #"+ jCurrentLI.text(),   text: "¡¡Muchas Felicidades!!",   imageUrl: "/static/img/winner.png" });



				} else {

					// Not done yet, call again shortly.
					setTimeout( Ticker, intPause );

				}
			}


			// Start ticker.
			Ticker();
		}

