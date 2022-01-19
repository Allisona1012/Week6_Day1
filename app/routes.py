from app import app
from flask import render_template
from app.forms import RegisterForm

@app.route('/')
def index():
    my_name = 'allison'
    return render_template('index.html')

@app.route('/book', methods = ["GET","POST"])
def book():
    form = RegisterForm()
    if form.validate_on_submit():
        print('FORM HAS BEEN VALIDATED!')
    return render_template('book.html', form = form)