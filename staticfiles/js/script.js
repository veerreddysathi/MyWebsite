$(document).ready(main);

function main() {
	
	$(document).ready(function() {
		$('.progress .progress-bar').css("width",
					function() {
						return $(this).attr("aria-valuenow") + "%";
					}
			)
		});

}