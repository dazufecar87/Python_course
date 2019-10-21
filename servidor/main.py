from flask import Flask

app = Flask(__name__) # nos pide que primero le enviemos como su constructor el nimbre del modulo


@app.route('/')
def hello_world():
    return 'Hola, mundo.'


if __name__ == '__main__':
    app.run()