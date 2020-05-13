"""Blueprint for game play"""

from flask import (Blueprint,
                   render_template,
                   redirect,
                   url_for,
                   request,
                   )

from ... gameprocessing.menu import (scorepad_available_scores,
                                     menu_items,
                                     )

from ... gameprocessing.scoring import (process_category_selection,
                                        score_number_of_a_kind,
                                        fixed_scores,
                                        )

from ... gameprocessing.play_game import game_status

from ... diceroll.dice import (die_roll,
                               dice_png,
                               roll_five_dice,
                               dice_png_list,
                               )

from .. forms import (DiceHoldWeb,
                      CategorySelect,
                      )

from .. config import scorepad_global

webgame_bp = Blueprint('webgame_bp',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='webgame',
                       )


def initialize_scorepad():
    """Reset scorepad attributes to initial values"""

    scorepad_global.web_turn_tracking = 0
    scorepad_global.web_dice_list = []
    scorepad_global.web_dice_list_hold = []
    attribute_exclude = ['upper_section_total',
                         'upper_section_total_show',
                         'upper_section_total_and_bonus',
                         'upper_section_bonus_calc',
                         'lower_section_total',
                         ]

    for _ in dir(scorepad_global):
        if _ not in attribute_exclude:
            if _.startswith('upper') or _.startswith('lower') or _.startswith('track'):
                # set to zero
                print(_, end='')
                setattr(scorepad_global, _, 0)  # How to set an attribute

        if _.startswith('zeroed'):
            # set to space here
            setattr(scorepad_global, _, ' ')
    print(f'****** INIT COMPLETE *******')

# Web turn tracking label
web_turn = ('First',
            'Second',
            'Third',
            )


@webgame_bp.route('/web_start_game', methods=['GET', 'POST'])
def web_start_game():

    """Web main function to initiate game."""

    if request.method == 'GET':

        # Use global object for scorepad

        print(f'scorepad_global: {scorepad_global}')
        print(f'scorepad_global.web_turn_tracking: {scorepad_global.web_turn_tracking}')

        try:
            web_turn_label = web_turn[scorepad_global.web_turn_tracking]
        except IndexError:
            print('Web turn Label Index out of range...')

        if scorepad_global.web_turn_tracking == 0:

            # Roll five dice for first turn
            scorepad_global.web_dice_list = roll_five_dice()
            scorepad_global.web_dice_list = sorted(scorepad_global.web_dice_list)

        print(f'******* {web_turn_label} ROLL ROUTE 00 **************')

        print(f'scorepad.web_dice_list before submit: {scorepad_global.web_dice_list}')

    # scorepad = scorepad_global
    web_turn_label = web_turn[scorepad_global.web_turn_tracking]
    # dice_hold_web_form = DiceHoldWeb()  # Not in use, but keep for now
    png_list = dice_png_list(scorepad_global.web_dice_list)

    print(f'png_list: {png_list}')

    print(f'******* {web_turn_label} ROLL ROUTE 01 **************')

    if request.method == 'POST':

        print(f'^^^^^^ POST ^^^^^^^')

        # Grab selected dice to keep from request form
        keep_dice = request.form

        print(f'keep_dice: {keep_dice}')

        for _ in keep_dice:
            print(f'{_} >>> {keep_dice[_]}')

        dice_list = scorepad_global.web_dice_list
        dice_list_hold = scorepad_global.web_dice_list_hold

        dice_list_hold = []
        dice_roll = []

        # Dice that are checked in form get added to dice_list_hold
        for _ in keep_dice:
            dice_list_hold.append(dice_list[int(keep_dice[_]) - 1])

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
        scorepad_global.web_dice_list = dice_roll

        scorepad_global.web_turn_tracking += 1

        if scorepad_global.web_turn_tracking <= 2:
            return redirect(url_for('webgame_bp.web_start_game',
                                    ))
        else:

            return redirect(url_for('webgame_bp.score_display_and_select',
                                    scorepad=scorepad_global,
                                    png_list=png_list,
                                    ))

    return render_template('webgame/roll_one.html',
                           scorepad=scorepad_global,
                           png_list=png_list,
                           # dice_hold_web_form=dice_hold_web_form,
                           web_turn_label=web_turn_label,
                           )


@webgame_bp.route('/score_display_and_select')
def score_display_and_select():
    """Display current score. Prompt for score category selection."""

    dice_list = sorted(scorepad_global.web_dice_list)
    png_list = dice_png_list(scorepad_global.web_dice_list)

    menu_list_build = []
    menu_list = []
    score_status = dict
    score_status = scorepad_available_scores(scorepad_global)

    display_flag = 'SELECT'

    for _ in score_status['AVAILABLE']:
        menu_list_build.append(menu_items[_])

    # If Five of a Kind bonus has been scored and the score is not
    # zero, append bonus counter since it does not have track prefix
    if scorepad_global.track_kind_five_of == 1 and scorepad_global.lower_kind_five_of != 0:
        # Only add bonus choice if dice being scored is a five of a kind
        if score_number_of_a_kind(dice_list,
                                  5,
                                  scorepad_global,
                                  ) == fixed_scores['score_kind_five_of']:
            menu_list_build.append([14, 'H - Five of a Kind Bonus'])

    # Strip character key used in command line version of dice-cvn
    menu_list_build = sorted(menu_list_build)
    for _ in menu_list_build:
        menu_list.append([_[1][0], _[1][4:len(_[1]) + 1]])

    category_select_form = CategorySelect()

    return render_template('webgame/score_display_and_select.html',
                           scorepad=scorepad_global,
                           dice_list=dice_list,
                           png_list=png_list,
                           category_select_form=category_select_form,
                           menu_list=menu_list,
                           display_flag=display_flag,
                           )


@webgame_bp.route('/update_scorepad/<selection>')
def update_scorepad(selection):
    print(f'***** update_scorepad route 03 *****')
    print(f'Selection key:  {selection}')

    final_dice = scorepad_global.web_dice_list
    png_list = dice_png_list(final_dice)

    scorepad = process_category_selection(final_dice,
                                          selection,
                                          scorepad_global,
                                          )
    display_flag = 'UPDATED'

    # Check if category selection is the last one. If true, go directly to
    # end of game route

    score_status = dict
    score_status = scorepad_available_scores(scorepad_global)

    if len(score_status['AVAILABLE']) == 0:
        return redirect(url_for('webgame_bp.end_of_game'))
    else:
        return render_template('webgame/score_display_and_select.html',
                               scorepad=scorepad_global,
                               dice_list=final_dice,
                               png_list=png_list,
                               display_flag=display_flag,
                               )


@webgame_bp.route('/next_turn')
def next_turn():
    """Check if player has updated all score categories. If not, reset
    turn tracking and dice list and start next turn. Otherwise show
    final score."""

    if game_status(scorepad_global):
        scorepad_global.web_turn_tracking = 0
        scorepad_global.web_dice_list = []
        return redirect(url_for('webgame_bp.web_start_game'))
    else:
        return redirect(url_for('webgame_bp.end_of_game'))


@webgame_bp.route('/end_of_game')
def end_of_game():
    """End game with display of final score and button to start a new
    game."""

    display_flag = 'END_OF_GAME'

    return render_template('webgame/score_display_and_select.html',
                           scorepad=scorepad_global,
                           display_flag=display_flag,
                           )


@webgame_bp.route('/exit_game')
def exit_game():
    """Render template if player quits in middle of game."""

    return render_template('webgame/exit_game.html')


@webgame_bp.route('/', methods=['GET', 'POST'])
@webgame_bp.route('/start_new_game')
def start_new_game():
    """reset scorepad"""

    initialize_scorepad()

    print(f'*** start_new_game function end ***')
    return redirect(url_for('webgame_bp.web_start_game',))


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


