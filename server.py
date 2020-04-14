from flask import Flask, render_template
app = Flask(__name__)
print(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<username>')
def custom(username=None):
    return render_template('custom.html', name=username)