"""Input player selection of score category to assign based on the
    dice held.
"""

from . scoring import process_category_selection

from . menu import menu_categories

from .. scorekeeping.scorepad import Scorepad_
from .. scorekeeping.scoredisplay import show_current_score


# Valid Menu Item Keys
valid_keys = ['1',
              '2',
              '3',
              '4',
              '5',
              '6',
              'A',
              'B',
              'C',
              'D',
              'E',
              'F',
              'G',
              'H',
              ]


def get_player_selection(scorepad):
    """Prompt player for category choice for scoring to update scorepad
    """

    while True:
        user_choice = input('Please enter your choice by entering the menu item key: ')

        if user_choice.upper() in valid_keys and user_choice.upper() in scorepad.available_choices:
            return user_choice
        else:
            print('Invalid item choice. Please try again.')


def scorepad_add_new_score(final_dice,
                           user_choice,
                           scorepad,
                           ):
    """Pass dice, user choice to update scorepad object
    """
    return process_category_selection(final_dice,
                                      selection,
                                      scorepad,
                                      )


if __name__ == '__main__':

    testpad = Scorepad_('tester')
    # final_dice = [1, 1, 2, 2, 2]
    final_dice = [1, 1, 2, 2, 3]

    print(final_dice)

    show_current_score(testpad,
                       testpad.upper_section_total(),
                       testpad.upper_section_bonus_calc(),
                       testpad.upper_section_total_and_bonus(),
                       testpad.lower_section_total(),
                       testpad.grand_total(),
                       )

    menu_categories(testpad)

    selection = get_player_selection()

    print()
    print(f'User entry is: {selection.upper()}')
    print()

    testpad = process_category_selection(final_dice, selection, testpad)

    show_current_score(testpad,
                       testpad.upper_section_total(),
                       testpad.upper_section_bonus_calc(),
                       testpad.upper_section_total_and_bonus(),
                       testpad.lower_section_total(),
                       testpad.grand_total(),
                       )

    print()
    print('*** END TEST ***')
