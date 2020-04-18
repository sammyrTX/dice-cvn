"""framework for web app version of dice-cvn game"""

from flask import (Flask,
                   render_template,
                   )

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # '<h1>Hello World</h1'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}</h1>'


if __name__ == '__main__':
    app.run()
