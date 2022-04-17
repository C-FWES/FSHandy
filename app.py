from flask import Flask, render_template, request
from suggest import suggest_route, format

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
    suggested = suggest_route()
    formatted = format(suggested)
    return render_template('suggestions.html', suggestions=formatted)


if __name__ == '__main__':
    app.run()
