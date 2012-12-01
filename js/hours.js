var WEEKS = 14;
var DAYS = 5;

$(document).ready(function(){
	addRowColHandlers();
	$('.day[rel]').overlay();
});

function addRowColHandlers() {
	var table = $('#week_table');
	var rows = table.find('.week_hours');
	for (i = 0; i < WEEKS; i++) {
		var row = rows[i];
		var days = 	$(row).find('.log_day');
		for (j = 0; j < DAYS; j++) {
			var day = days[j];
			var box = $(day);
			
			var bf = (function(fi, fj) {
				return function() {
					addHours(fi, fj);
				}
			})(i + 1, j);
			
			box.click(bf);
		}
	}
};

function addHours(week, day) {
//	console.log(week + "," + day);
	var activeForm = document.getElementById('main-form');
	activeForm.elements[0].value = WEEK_KEYS[week - 1];
	activeForm.elements[1].value = day;
}

function submitForm(type) {
	var activeForm = document.getElementById('main-form');
	var name = type.name;
	if (name == "addForm") {
		activeForm.action="/addhours";
	}
	else if (name == "delForm") {
		activeForm.action="/delhours";
		activeForm.submit()
	}
}
