my_url = "http://sf-pyw.mosyag.in/m04/api/forecasts"

function hc() {

	$.getJSON(my_url, function(prophecies) {
		console.log("Пришло")
		mes = prophecies["prophecies"]
		set_content_in_divs(mes);
		console.log(prophecies)

	});

}

function set_content_in_divs(paragraphs) {
  	$.each(paragraphs, function(i, d) {
    p = $("#p-" + i)
    p.html("<p>" + d + "</p>")
  	})
}
