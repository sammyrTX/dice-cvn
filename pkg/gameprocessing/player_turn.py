"""Process game play"""

import os
from .. diceroll.dice import die_roll
from .. diceroll.dicegraphic import dice_display

from . menu import menu_categories
from . score_selection import get_player_selection
from . score_selection import process_category_selection

from .. scorekeeping.scorepad import Scorepad_
from .. scorekeeping.scoredisplay import show_current_score


def request_dice_to_keep():

    while True:
        try:
            print('Enter dice to keep. "Q" to keep all dice and quit turn.')
            dice_list_hold_idx = input('Dice to keep?: ')
            if dice_list_hold_idx[0].upper() == 'Q':
                print('Quitting turn...')
            return dice_list_hold_idx
        except IndexError:
            print('Please enter a valid item key.')


def store_dice_to_keep(dice_list_hold_idx, dice_roll):
    dice_list_hold = []

    if dice_list_hold_idx[0].upper() == 'Q':
        return dice_list_hold

    for hold in dice_list_hold_idx:
        dice_list_hold.append(dice_roll[int(hold) - 1])
    return dice_list_hold


def get_and_store_dice_to_keep(dice_roll):
    dice_list_hold_idx = request_dice_to_keep()
    dice_list_hold = store_dice_to_keep(dice_list_hold_idx, dice_roll)
    return (dice_list_hold_idx,
            dice_list_hold,
            )


def player_turn(scorepad):
    """This section generates the dice rolls and processes the scoring for the
    dice that are kept.
    """

    # Lists to store initial rolls and final dice

    dice_roll = []
    dice_list_hold = []
    dice_list_hold_idx = []
    final_dice = []
    new_dice_qty = 0

    # Player turn
    # Three rolls per turn

    while True:
        # Roll One - roll all five dice

        print('First Roll:')

        # First roll is all five dice
        for roll1 in range(1, 6):
            dice_roll.append(die_roll())

        # Show dice
        dice_roll = sorted(dice_roll)
        dice_display(dice_roll)

        # Get dice to keep and store for next roll
        (dice_list_hold_idx,
         dice_list_hold,
         ) = get_and_store_dice_to_keep(dice_roll)

        # Proceed to second roll if not quitting turn after first roll
        if dice_list_hold_idx[0].upper() != 'Q':

            # reset for next dice roll
            dice_roll = []

            # Roll Two - roll dice not kept

            print()
            os.system('clear')
            print('Second Roll:')

            # Get quantity of dice to roll next
            new_dice_qty = 5 - len(dice_list_hold)

            # Add dice that were kept to the new set of dice
            for keep_die in dice_list_hold:
                dice_roll.append(int(keep_die))

            # Roll dice that were not kept and add to the list
            for roll2 in range(1, (new_dice_qty + 1)):
                dice_roll.append(die_roll())

            # Show dice
            dice_roll = sorted(dice_roll)
            dice_display(dice_roll)

        if dice_list_hold_idx[0].upper() != 'Q':
            # Roll Three - roll dice not kept

            # Clear dice previously held and request new dice to keep
            dice_list_hold = []

            (dice_list_hold_idx,
             dice_list_hold,
             ) = get_and_store_dice_to_keep(dice_roll)

            # Proceed to third roll if not quitting turn after second roll
            if dice_list_hold_idx[0].upper() != 'Q':

                # reset for next dice roll
                dice_roll = []

                print()
                os.system('clear')
                print('Third Roll:')

                new_dice_qty = 5 - len(dice_list_hold)

                # Add dice that were kept to the new set of dice
                for keep_die in dice_list_hold:
                    dice_roll.append(int(keep_die))

                for next_roll in range(1, (new_dice_qty + 1)):
                    dice_roll.append(die_roll())

                # Show dice
                dice_roll = sorted(dice_roll)
                dice_display(dice_roll)

        final_dice = dice_roll

        # Show dice being held for scoring
        os.system('clear')
        print()
        print('Here are the dice to be scored:')
        print()

        dice_display(final_dice)
        print()

        print('Current Score:')

        show_current_score(scorepad,
                           scorepad.upper_section_total(),
                           scorepad.upper_section_bonus_calc(),
                           scorepad.upper_section_total_and_bonus(),
                           scorepad.lower_section_total(),
                           scorepad.grand_total(),
                           )

        # Proceed to scoring
        # Assign dice to score category

        # Display a menu of available score categories

        menu_categories(scorepad)

        # Prompt and input player selection
        selection = get_player_selection()

        # Process score
        scorepad = process_category_selection(final_dice,
                                              selection,
                                              scorepad,
                                              )

        # Show updated score
        show_current_score(scorepad,
                           scorepad.upper_section_total(),
                           scorepad.upper_section_bonus_calc(),
                           scorepad.upper_section_total_and_bonus(),
                           scorepad.lower_section_total(),
                           scorepad.grand_total(),
                           )

        # End of turn
        # Prompt to start next roll
        input('Press enter to continue')
        print('Exiting turn...')
        return scorepad
        # break


if __name__ == '__main__':

    # Name input needs to be either in a main starting point module or
    # as a mini function

    # Request player name and instanciate scorepad_ object
    scorepad = Scorepad_(input('Please enter your name: '))

    while True:

        player_turn(scorepad)
        input('Press enter to continue')
        break

    print('*** Ready for next turn ***')
