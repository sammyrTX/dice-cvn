"""Generate menu of available score category choices after completing
dice roll turn.

Menu Choices

Key     Description
 1      Ones
 2      Twos
 3      Threes
 4      Fours
 5      Fives
 6      Sixes
 A      Three of a Kind
 B      Four of a Kind
 C      Full House
 D      Small Straight
 E      Large Straight
 F      Five of a Kind
 G      Any Dice
 H      Five of a Kind Bonus
"""

# Menu List

menu_items = {'track_ones': [1, '1 - Ones'],
              'track_twos': [2, '2 - Twos'],
              'track_threes': [3, '3 - Threes'],
              'track_fours': [4, '4 - Fours'],
              'track_fives': [5, '5 - Fives'],
              'track_sixes': [6, '6 - Sixes'],
              'track_kind_three_of': [7, 'A - Three of a Kind'],
              'track_kind_four_of': [8, 'B - Four of a Kind'],
              'track_full_house': [9, 'C - Full House'],
              'track_straight_small': [10, 'D - Small Straight'],
              'track_straight_large': [11, 'E - Large Straight'],
              'track_kind_five_of': [12, 'F - Five of a Kind'],
              'track_all_dice': [13, 'G - Any Dice'],
              'track_bonus': [14, 'H - Five of a Kind Bonus'],
              }


def menu_categories(scorepad):
    """Based on scorepad tracking of items that have not been scored,
    build and display only categories that have not already been assigned.
    """

    available_choices = []
    menu_list = []

    for _ in dir(scorepad):
        if _.startswith('track'):
            if getattr(scorepad, _) == 0:
                available_choices.append(_)

    for _ in available_choices:
        menu_list.append(menu_items[_])

    print('=' * 50)

    print('MENU LIST (sorted)')

    for idx, _ in enumerate(sorted(menu_list)):

        if (idx + 1)%2 == 0:
            print(_[1])
        else:
            pad = 25 - len(_[1])
            print(_[1], end=(' ' * pad))


if __name__ == '__main__':

    from .. scorekeeping.scorepad import Scorepad_

    testpad = Scorepad_('tester')

    testpad.upper_fives = 50
    testpad.track_ones = 1
    testpad.track_twos = 1
    testpad.track_threes = 1
    testpad.track_fours = 1
    testpad.track_fives = 1
    testpad.track_sixes = 1

    menu_categories(testpad)

