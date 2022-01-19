from app import app
from flask import render_template

@app.route('/')
def index():
    my_name = 'allison'
    return render_template('index.html')

@app.route('/name')
def name():
    my_name = 'allison'
    return f'Hello {my_name}'