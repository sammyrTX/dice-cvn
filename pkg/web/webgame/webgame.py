"""Blueprint for game play"""

from flask import (Blueprint,
                   render_template,
                   redirect,
                   url_for,
                   )

from ... scorekeeping.scorepad import Scorepad_

from ... diceroll.dice import (die_roll,
                               dice_png,
                               )

from .. forms import (DiceHold,
                      DiceHoldWeb,
                      )

webgame_bp = Blueprint('webgame_bp',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='webgame',
                       )


@webgame_bp.route('/', methods=['GET', 'POST'])
def web_start_game():

    # *** Resume here to manage game play for players turn***
    # coninue working on rendering HTML after first roll and then gather
    # player selections for dice to hold
    # Also need to store dice values kept and add to new rolls

    """Web main function to initiate game."""

    # Instantiate scorepad_ object
    scorepad = Scorepad_('Player01')

    # Roll five dice for first turn
    for _ in range(1, 6):
        scorepad.web_dice_list.append(dice_png[die_roll() - 1])

    scorepad.web_dice_list = sorted(scorepad.web_dice_list)

    print(f'scorepad.web_dice_list before submit: {scorepad.web_dice_list}')

    dice_hold_web_form = DiceHoldWeb()

    scorepad.web_turn_tracking = 888
    scorepad.track_fours = 21

    if dice_hold_web_form.validate_on_submit():

        die1 = dice_hold_web_form.die1.data
        die2 = dice_hold_web_form.die2.data
        die3 = dice_hold_web_form.die3.data
        die4 = dice_hold_web_form.die4.data
        die5 = dice_hold_web_form.die5.data

        dice_hold_web_form.die1.data = ''
        dice_hold_web_form.die2.data = ''
        dice_hold_web_form.die3.data = ''
        dice_hold_web_form.die4.data = ''
        dice_hold_web_form.die5.data = ''

        scorepad.web_turn_tracking = 999
        scorepad.track_fours = 32

        print(f'scorepad.web_dice_list after submit: {scorepad.web_dice_list}')
        dice_list = scorepad.web_dice_list

        # dice_hold = testform.dice_hold.data
        # testform.dice_hold.data = ''

        return redirect(url_for('webgame_bp.roll_two',
                                die1=die1,
                                scorepad=scorepad,
                                web_turn_tracking=scorepad.web_turn_tracking,
                                dice_list=dice_list,
                                ))
        # return render_template('roll_two.html',
        #                        die1=die1,
        #                        scorepad=scorepad,
        #                        web_turn_tracking=scorepad.web_turn_tracking,
        #                        dice_list=dice_list,
        #                        )

    return render_template('webgame/roll_one.html',
                           scorepad=scorepad,
                           dice_hold_web_form=dice_hold_web_form,
                           track_fours=scorepad.track_fours,
                           )





# Sample Blueprint code

# products_bp = Blueprint('products_bp', __name__,
#     template_folder='templates',
#     static_folder='static', static_url_path='assets')

# @products_bp.route('/')
# def list():
#     products = Product.query.all()
#     return render_template('products/list.html', products=products)

# @products_bp.route('/view/<int:product_id>')
# def view(product_id):
#     product = Product.query.get(product_id)
#     return render_template('products/view.html', product=product)



# @webgame_bp.route('/roll_one/<scorepad>/<dice_list>/<turn_track>')
# def roll_one(scorepad, dice_list, turn_track):
#     """First roll of a turn. Roll all five dice"""

#     print('******** roll one route ************')
#     print(f'scorepad.dice_list: {scorepad.dice_list}')
#     # turn_track = scorepad.web_turn_tracking
#     scorepad.web_turn_tracking = 99

#     return render_template('roll_one.html',
#                            scorepad=scorepad,
#                            dice_list=dice_list,
#                            turn_track=scorepad.web_turn_tracking,
#                            )


@webgame_bp.route('/roll_two/<scorepad>/<die1>/<web_turn_tracking>')
def roll_two(scorepad, die1, web_turn_tracking):
    """Second roll of a turn. Roll up to five dice"""
    print(f'******* ROLL TWO ROUTE **************')
    print(f'die1: {die1}')
    print(f'scorepad: {scorepad}')
    print(f'web_turn_tracking: {web_turn_tracking}')

    # dice_list = ['images/dice3.png', 'images/dice3.png', 'images/dice2.png', 'images/dice3.png', 'images/dice3.png']

    return render_template('roll_two.html',
                           scorepad=scorepad,
                           dice_list=dice_list,
                           die1=die1,
                           web_turn_tracking=web_turn_tracking,
                           # turn_track=scorepad.web_turn_tracking,
                           )


@webgame_bp.route('/roll_three')
def roll_three():
    """Third roll of a turn. Final dice. Proceed to scoring."""
    pass


@webgame_bp.route('/score_display_and_select')
def score_display_and_select():
    """Display current score. Prompt for score category selection."""
    pass


@webgame_bp.route('/score_display_updated')
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
