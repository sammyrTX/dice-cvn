"""framework for web app version of dice-cvn game"""

from flask import (Flask,
                   render_template,
                   )

from . forms import DiceHold

from .. diceroll.dice import die_roll
from .. gameprocessing.play_game import (start_game,
                                         game_status,
                                         web_player_turn,
                                         )
from .. scorekeeping.scorepad import Scorepad_



app = Flask(__name__)

app.config['SECRET_KEY'] = 'toASMuE59soIk7*9jA*F'


@app.route('/')
def index():
    return render_template('index.html')  # '<h1>Hello World</h1'

# *** Resume here to manage game play for players turn***


@app.route('/web_start_game')
def web_start_game():
    pass
    """Web main function to initiate and handle entire game."""

    # Request player name and instantiate scorepad_ object
    scorepad = Scorepad_('Player01')

    while True:

        while True:
            scorepad = web_player_turn(scorepad)

            if game_status(scorepad):
                continue
            else:
                break
        break

########################################################################
    # *** Build template to replace CLI code below

    print('Final Score:')

    show_current_score(scorepad,
                       scorepad.upper_section_total(),
                       scorepad.upper_section_bonus_calc(),
                       scorepad.upper_section_total_and_bonus(),
                       scorepad.lower_section_total(),
                       scorepad.grand_total(),
                       )
    print()
    print(f'Thanks for playing! Your final score is {scorepad.grand_total()}')
    print()
########################################################################


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}</h1>'


@app.route('/game_display', methods=['GET', 'POST'])
def game_display():

    form = DiceHold()

    dice_hold = 0
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

    if form.validate_on_submit():
        dice_hold = form.dice_hold.data
        form.dice_hold.data = ''

    return render_template('game_display.html',
                           dice_list=dice_list,
                           form=form,
                           dice_hold=dice_hold,
                           )

    # return render_template('game_display.html')


@app.route('/exit_game')
def exit_game():
    return render_template('exit_game.html')



if __name__ == '__main__':
    app.run()
