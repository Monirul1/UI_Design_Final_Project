google.charts.load('current', { packages: [ 'corechart' ] });
google.charts.setOnLoadCallback(drawChart);

let dashboard_data_grocery = [
    ['Used', 250],
    ['Remaining', 120],
]

let dashboard_data_dining = [
    ['Used', 400],
    ['Remaining', 50],
]

let dashboard_data_utility = [
    ['Used', 150],
    ['Remaining', 50],
]

let dashboard_data_transportation = [
    ['Used', 150],
    ['Remaining', 80],
]

function drawChart() {
	// chart1
    charHelper('Grocery', dashboard_data_grocery, 'piechart_grocery')
	// draw2
    charHelper('Dining', dashboard_data_dining, 'piechart_dining')
	// draw3
    charHelper('Utility', dashboard_data_utility, 'piechart_utility')
	// draw4
    charHelper('Transportation', dashboard_data_transportation, 'piechart_transportation')
}

function charHelper(title, raw_data, chart_id) {
    var data = new google.visualization.DataTable();
    data.addColumn('string','Title');
    data.addColumn('number','Amount');
    data.addRows(raw_data);

    var total = raw_data.reduce((x, y) => x[1] + y[1]);

	var options = {
		legend: 'none',
		pieSliceText: 'label',
		title:
			`${title}: Budget $${total}, Remaining $${ raw_data[1][1] }`,
		pieStartAngle: 100,
        backgroundColor: 'transparent',
	};

	var chart = new google.visualization.PieChart(document.getElementById(chart_id));
	chart.draw(data, options);
}
