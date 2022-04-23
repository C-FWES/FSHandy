from flask import Flask, render_template, request
import requests
import urllib.request, json

from urllib3.util import url

import frequencies
from suggest import suggest_route, format
from frequencies import get_frequencies, format_freq

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
    # r = requests.get('https://avwx.rest/api/metar/' + icao + '?options=&airport=true&reporting=true&format=json&onfail=cache?token=XbkdYIntZ6Xo9BUMA_x_vuaG8_zRZCWZVOEOFkCpl2Q')
    # json_data = xmltodict.parse(r.content)
    metar = ""
    url_str = 'https://avwx.rest/api/metar/' + icao + '?token=XbkdYIntZ6Xo9BUMA_x_vuaG8_zRZCWZVOEOFkCpl2Q'
    with urllib.request.urlopen(url_str) as info:
        data = json.loads(info.read().decode())
        metar = data['sanitized']
    return render_template('weather_results.html', metar=metar)

@app.route('/perf')
def perf():
    return render_template('perf.html')

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
