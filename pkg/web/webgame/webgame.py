"""Blueprint for game play"""

from flask import (Blueprint,
                   render_template,
                   redirect,
                   url_for,
                   request,
                   )

from ... scorekeeping.scorepad import Scorepad_

from ... diceroll.dice import (die_roll,
                               dice_png,
                               roll_five_dice,
                               dice_png_list,
                               )

from .. forms import (DiceHold,
                      DiceHoldWeb,
                      RollTwo,
                      )

from .. config import scorepad_global

webgame_bp = Blueprint('webgame_bp',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='webgame',
                       )

# Web turn tracking label
web_turn = ('First',
            'Second',
            'Third',
            )


@webgame_bp.route('/', methods=['GET', 'POST'])
def web_start_game():

    """Web main function to initiate game."""

    if request.method == 'GET':

        # Set local variable to global object for scorepad
        scorepad_local = scorepad_global
        print(f'scorepad_local: {scorepad_local}')
        print(f'scorepad_local.web_turn_tracking: {scorepad_local.web_turn_tracking}')

        try:
            web_turn_label = web_turn[scorepad_local.web_turn_tracking]
        except IndexError:
            print('Web turn Label Index out of range...')

        if scorepad_local.web_turn_tracking == 0:

            # Roll five dice for first turn
            scorepad_local.web_dice_list = roll_five_dice()
            scorepad_local.web_dice_list = sorted(scorepad_local.web_dice_list)

        print(f'******* {web_turn_label} ROLL ROUTE **************')

        print(f'scorepad.web_dice_list before submit: {scorepad_local.web_dice_list}')

    scorepad = scorepad_global
    web_turn_label = web_turn[scorepad.web_turn_tracking]
    dice_hold_web_form = DiceHoldWeb()
    png_list = dice_png_list(scorepad.web_dice_list)

    print(f'png_list: {png_list}')

    print(f'******* {web_turn_label} ROLL ROUTE **************')

    if dice_hold_web_form.validate_on_submit():

        die1 = dice_hold_web_form.die1.data
        die2 = dice_hold_web_form.die2.data
        die3 = dice_hold_web_form.die3.data
        die4 = dice_hold_web_form.die4.data
        die5 = dice_hold_web_form.die5.data

        dice_list = scorepad.web_dice_list
        dice_list_hold = scorepad.web_dice_list_hold

        print(f'die1: {die1}')
        print(f'die2: {die2}')
        print(f'die3: {die3}')
        print(f'die4: {die4}')
        print(f'die5: {die5}')

        dice_hold_web_form.die1.data = ''
        dice_hold_web_form.die2.data = ''
        dice_hold_web_form.die3.data = ''
        dice_hold_web_form.die4.data = ''
        dice_hold_web_form.die5.data = ''

        dice_list_hold = []
        dice_roll = []

        # Dice that are checked in form get added to dice_list_hold
        if die1:
            dice_list_hold.append(dice_list[0])

        if die2:
            dice_list_hold.append(dice_list[1])

        if die3:
            dice_list_hold.append(dice_list[2])

        if die4:
            dice_list_hold.append(dice_list[3])

        if die5:
            dice_list_hold.append(dice_list[4])

        print('*' * 45)
        print(f'dice_list_hold_check: {dice_list_hold}')
        print('*' * 45)

        # Get quantity of dice to roll next
        new_dice_qty = 5 - len(dice_list_hold)

        # Add dice that were kept to the new set of dice
        for keep_die in dice_list_hold:
            dice_roll.append(int(keep_die))

        # Roll dice that were not kept and add to the list and then sort
        for roll2 in range(1, (new_dice_qty + 1)):
            dice_roll.append(die_roll())

        dice_roll = sorted(dice_roll)

        print('*' * 45)
        print(f'{web_turn_label} dice_roll check: {dice_roll}')
        print('*' * 45)

        # Store second roll dice back into the global object
        scorepad.web_dice_list = dice_roll

        scorepad.web_turn_tracking += 1

        if scorepad.web_turn_tracking <= 2:
            return redirect(url_for('webgame_bp.web_start_game',
                                    ))
        else:

            return redirect(url_for('webgame_bp.score_display_and_select',
                                    scorepad=scorepad,
                                    ))

    return render_template('webgame/roll_one.html',
                           scorepad=scorepad,
                           png_list=png_list,
                           dice_hold_web_form=dice_hold_web_form,
                           web_turn_label=web_turn_label,
                           )


@webgame_bp.route('/score_display_and_select')
def score_display_and_select():
    """Display current score. Prompt for score category selection."""
    scorepad = scorepad_global
    dice_list = sorted(scorepad.web_dice_list)
    png_list = dice_png_list(scorepad.web_dice_list)

    return render_template('webgame/score_display_and_select.html',
                           scorepad=scorepad,
                           dice_list=dice_list,
                           png_list=png_list,
                           )


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
