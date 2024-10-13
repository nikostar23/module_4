from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

@app.route('/hello')
def hello_world():
    name = request.args.get('name', 'World')
    surname = request.args.get('surname', 'User')
    return f'Hello {name} {surname}!'

def get_all_users_form_db():
    return [
        {
            "id": 1,
            "username": "Alice",
            "email": "alice@mail.ru"
        },
        {
            "id": 23,
            "username": "Boris",
            "email": "boris@yandex.ru"
        }
    ]

@app.route('/users')
def get_users():
    users = []
    for user in get_all_users_form_db():
        users.append(user)
    return jsonify(users)


if __name__ == '__main__':
    app.run()
