from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__, template_folder='template')

software = []
hardware = []

@app.route('/alerts', methods= ['POST', 'GET'])
def alerts():
	if request.method == 'POST':
		req_data = request.get_json()
		metric_alerts = 'alerts' in req_data
		logs_alerts = 'type' in req_data
		if metric_alerts:
			metrics_alert_data = req_data['alerts']
			for malerts in metrics_alert_data:
				hardware.append(malerts)
			mdisplay = ''
			with open('template/alert_display.html','w') as m:
				mdisplay = 'Metric Alert sent!'
				m.write(mdisplay)
			return ''

		elif logs_alerts:
			software.append(req_data)
			ldisplay = ''
			with open('template/alert_display.html','w') as l:
				ldisplay = 'Logs alert sent!'
				l.write(ldisplay)
			return ''


	return render_template('alert_display.html')


@app.route('/graph')
def graph():
	for i in hardware:
		print(i['status'])
	return render_template('graph.html', software_alerts=software, hardware_alerts = hardware)

if __name__ == '__main__':

	app.run(host='0.0.0.0', debug=True)

