"""framework for web app version of dice-cvn game"""

from flask import (Flask,
                   render_template,
                   )

from .. diceroll.dice import die_roll



app = Flask(__name__)
# app = Flask(__name__,  static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')  # '<h1>Hello World</h1'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}</h1>'


@app.route('/game_display')
def game_display():

    dice_list = []
    dice_list_hold = []
    dice_png = ['images/dice1.png',
                'images/dice2.png',
                'images/dice3.png',
                'images/dice4.png',
                'images/dice5.png',
                'images/dice6.png',
                ]

    die_roll()

    for _ in range(1, 6):

        # dice_list.append(die_roll())
        dice_list.append(dice_png[die_roll() - 1])

    dice_list = sorted(dice_list)

    print(f'dice_list: {dice_list}')

    return render_template('game_display.html',
                           dice_list=dice_list,
                           )

    # return render_template('game_display.html')


if __name__ == '__main__':
    app.run()
