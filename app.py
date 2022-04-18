from flask import Flask, render_template, request

import frequencies
from suggest import suggest_route, format
from frequencies import get_frequencies, format

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
    formatted = frequencies.format(freqs)
    return render_template('frequency_results.html', frequencies=formatted)


if __name__ == '__main__':
    app.run()
