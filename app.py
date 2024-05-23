from hi import fraz
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/hi')
def hi():
    x = fraz()
    return x