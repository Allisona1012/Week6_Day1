from app import app
from flask import render_template,redirect,url_for
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
        full_name= form.full_name.data
        email = form.email.data
        phone_number= form.phone_number.data
        return redirect(url_for('index'))


    return render_template('book.html', form = form)