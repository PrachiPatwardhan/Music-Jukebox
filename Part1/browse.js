function processMessage() {
        		var songname = $("#song").val();
        		var artistname = $('#artist').val();
        		/*document.getElementById("var1").innerHTML = songname;
        		document.getElementById("var2").innerHTML = artistname;
				*/
				$.ajax({
					type: 'POST',
					url: 'http://localhost/exten.py',
					data: {song:songname, artist:artistname},
					success: function(response) {
						link = response.substring(response.indexOf("http"),response.length - 1) 
						$('#download-button').attr({target: '_blank',  href  : link});
						console.log(link)
					}
       		});
       	}
