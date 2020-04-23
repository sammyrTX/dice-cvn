"""framework for web app version of dice-cvn game"""

from flask import (Flask,
                   render_template,
                   )

from . forms import DiceHold

from .. diceroll.dice import (die_roll,
                              dice_png,
                              )
from .. gameprocessing.web_player_turn import web_player_turn
from .. gameprocessing.play_game import (start_game,
                                         game_status,
                                         )
from .. scorekeeping.scorepad import Scorepad_

# Remove after HTML complete
from .. scorekeeping.scoredisplay import show_current_score



app = Flask(__name__)

app.config['SECRET_KEY'] = 'toASMuE59soIk7*9jA*F'


@app.route('/')
def index():
    return render_template('index.html')  # '<h1>Hello World</h1'


@app.route('/web_start_game')
def web_start_game():

# *** Resume here to manage game play for players turn***
# coninue working on rendering HTML after first roll and then gather
# player selections for dice to hold

    """Web main function to initiate game."""

    # Instantiate scorepad_ object
    scorepad = Scorepad_('Player01')

    # Roll five dice for first turn
    for _ in range(1, 6):
        scorepad.web_dice_list.append(dice_png[die_roll() - 1])

    scorepad.web_dice_list = sorted(scorepad.web_dice_list)

    scorepad.web_turn_tracking = 1

    testform = DiceHold()

    return render_template('roll_one.html',
                           scorepad=scorepad,
                           testform=testform,
                           )

@app.route('/roll_one/<scorepad>/<dice_list>/<turn_track>')
def roll_one(scorepad, dice_list, turn_track):
    """First roll of a turn. Roll all five dice"""
    dice_list = ['images/dice3.png', 'images/dice3.png', 'images/dice2.png', 'images/dice3.png', 'images/dice3.png']

    # turn_track = scorepad.web_turn_tracking
    scorepad.web_turn_tracking = 99

    return render_template('roll_one.html',
                           scorepad=scorepad,
                           dice_list=dice_list,
                           turn_track=scorepad.web_turn_tracking,
                           )


@app.route('/roll_two')
def roll_two():
    """Second roll of a turn. Roll up to five dice"""
    pass


@app.route('/roll_three')
def roll_three():
    """Third roll of a turn. Final dice. Proceed to scoring."""
    pass


@app.route('/score_display_and_select')
def score_display_and_select():
    """Display current score. Prompt for score category selection."""
    pass


@app.route('/score_display_updated')
def score_display_updated():
    """Display updated score. Proceed to roll one when ready if score
    categories are available. If all categories have been assigned, end
    game."""
    pass
########################################################################
    # *** Build template to replace CLI code below

    # print('Final Score:')

    # show_current_score(scorepad,
    #                    scorepad.upper_section_total(),
    #                    scorepad.upper_section_bonus_calc(),
    #                    scorepad.upper_section_total_and_bonus(),
    #                    scorepad.lower_section_total(),
    #                    scorepad.grand_total(),
    #                    )
    # print()
    # print(f'Thanks for playing! Your final score is {scorepad.grand_total()}')
    # print()
########################################################################

    return f'<h1>Return after completion of /web_start_game</h1>'


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
