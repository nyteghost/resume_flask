from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/layout/')
def header():
    return render_template('layout.html')


@app.route('/resume/')
def resume():
    return render_template('resume.html')


@app.route('/stats/')
def stats():
    return render_template('stats.html')


if __name__ == '__main__':
    app.run(debug=True)