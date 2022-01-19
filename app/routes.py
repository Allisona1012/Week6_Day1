from app import app

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/name')
def name():
    my_name = 'allison'
    return f'Hello {my_name}'