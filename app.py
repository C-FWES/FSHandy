from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run()
