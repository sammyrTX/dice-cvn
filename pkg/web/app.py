"""framework for web app version of dice-cvn game"""

from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   )

from . forms import (DiceHold,
                     DiceHoldWeb,
                     )

from .. diceroll.dice import (die_roll,
                              dice_png,
                              )
from .. gameprocessing.web_player_turn import web_player_turn
from .. gameprocessing.play_game import (start_game,
                                         game_status,
                                         )
from .. scorekeeping.scorepad import Scorepad_


from .. web.webgame.webgame import webgame_bp
from .. web.temptest.temptest import temptest_bp  # Test only - Remove

# Remove after HTML complete
from .. scorekeeping.scoredisplay import show_current_score


app = Flask(__name__)

app.config['SECRET_KEY'] = 'toASMuE59soIk7*9jA*F'

app.register_blueprint(webgame_bp, url_prefix='/webgame')
app.register_blueprint(temptest_bp, url_prefix='/temptest')  # Test only - Remove


@app.route('/')
def index():
    return render_template('index.html')  # '<h1>Hello World</h1'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}</h1>'


@app.route('/game_display', methods=['GET', 'POST'])
def game_display():

    formX = DiceHold()

    dice_hold = 0
    dice_list = []
    dice_list_hold = []
    # dice_png = ['images/dice1.png',
    #             'images/dice2.png',
    #             'images/dice3.png',
    #             'images/dice4.png',
    #             'images/dice5.png',
    #             'images/dice6.png',
    #             ]

    die_roll()

    for _ in range(1, 6):

        # dice_list.append(die_roll())
        dice_list.append(dice_png[die_roll() - 1])

    dice_list = sorted(dice_list)

    print(f'dice_list: {dice_list}')

    if formX.validate_on_submit():
        dice_hold = formX.dice_hold.data
        formX.dice_hold.data = ''

    return render_template('game_display.html',
                           dice_list=dice_list,
                           form=formX,
                           dice_hold=dice_hold,
                           )

    # return render_template('game_display.html')


@app.route('/exit_game')
def exit_game():
    return render_template('exit_game.html')



if __name__ == '__main__':
    app.run()
