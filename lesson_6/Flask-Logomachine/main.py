from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

@app.route('/world')
def world():
    return 'Я живу в Санкт-Петербурге. Наш город стоит на Неве. Эта река имеет длинну 74 км'

if __name__ == '__main__':
    app.run()
