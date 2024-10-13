from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

@app.route('/<x>/<y>/add')
def add(x, y):
    x, y = float(x), float(y)
    return f'{x} + {y} = {x + y}'

@app.route('/<x>/<y>/sub')
def sub(x, y):
    x, y = float(x), float(y)
    return f'{x} - {y} = {x - y}'

@app.route('/<x>/<y>/multi')
def multi(x, y):
    x, y = float(x), float(y)
    return f'{x} * {y} = {x * y}'

@app.route('/<x>/<y>/split')
def split(x, y):
    x, y = float(x), float(y)
    if y:
        return f'{x} / {y} = {x / y}'
    else:
        return "Недопустимое действие, делить на ноль нельзя"

if __name__ == '__main__':
    app.run()
