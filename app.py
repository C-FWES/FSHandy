from flask import Flask, render_template, request
import urllib.request, json
from suggest import suggest_route, format
from frequencies import get_frequencies, format_freq
from weather import format_runways, reccommend_runway
from perf import calculate_tod, calculate_descent_rate

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/convert')
def convert():
    return render_template('conversions.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/metar', methods=['GET', 'POST'])
def get_metar():
    icao = request.form.get('icao')
    metar = ""
    runways = []
    url_str = 'https://avwx.rest/api/metar/' + icao + '?token=XbkdYIntZ6Xo9BUMA_x_vuaG8_zRZCWZVOEOFkCpl2Q'
    urL_str_airfield = 'https://avwx.rest/api/station/' + icao + '?token=XbkdYIntZ6Xo9BUMA_x_vuaG8_zRZCWZVOEOFkCpl2Q'
    with urllib.request.urlopen(url_str) as info:
        data = json.loads(info.read().decode())
        metar = data['sanitized']
    with urllib.request.urlopen(urL_str_airfield) as station:
        data1 = json.loads(station.read().decode())
        runways = data1['runways']
    formatted_runways = format_runways(runways)
    reccomended_runway = reccommend_runway(runways, metar)
    format_reccomended = reccomended_runway[:2]
    if str(format_reccomended[1]) == '0':
        format_reccomended = '0' + format_reccomended[0]
    return render_template('weather_results.html', metar=metar, runways=formatted_runways, reccomended=format_reccomended)

@app.route('/perf')
def perf():
    return render_template('perf.html')

@app.route('/handle_perf', methods=['POST', 'GET'])
def handle_perf():
    start_alt = int(request.form.get('start_alt'))
    target_alt = int(request.form.get('end_alt'))
    ias_start = int(request.form.get('ias_start'))
    top_descent = calculate_tod(start_alt, target_alt)
    fpm = calculate_descent_rate(ias_start)
    return render_template('performance_results.html', tod=top_descent, fpm=fpm)

@app.route('/frequencies')
def freq():
    return render_template('frequencies.html')

@app.route('/suggestions', methods=['POST', 'GET'])
def suggest():
    return render_template('suggestions.html')

@app.route('/handle_suggestions', methods=['POST', 'GET'])
def handle():
    range_start = request.form['start']
    range_end = request.form['end']
    suggested = suggest_route(range_start, range_end)
    formatted = format(suggested)
    return render_template('results.html', suggestions=formatted)

@app.route('/handle_frequencies', methods=['POST', 'GET'])
def handle_freqs():
    icao = request.form['icao']
    freqs = get_frequencies(icao)
    formatted = format_freq(freqs)
    return render_template('frequency_results.html', frequencies=formatted)


if __name__ == '__main__':
    app.run()
