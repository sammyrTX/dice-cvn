"""Calculate score for all categories"""

import numpy as np

# Points for fixed score categories in Dict

fixed_scores = {'score_full_house': 25,
                'score_straight_small': 30,
                'score_straight_large': 40,
                'score_kind_five_of': 50,
                'upper_section_bonus': 35,
                }


def upper_section_score(die_value,
                        final_dice,
                        scorepad,
                        ):
    """Evaluate dice from a roll for a given value and multiply the count
    by that value. E.g. for a die value of 3 and a count of two dice with
    that value the total score is 6 (die value of 3 times a count of two)
    """

    if die_value in range(1, 7):
        return final_dice.count(die_value) * die_value
    else:
        return 0


def score_number_of_a_kind(final_dice,
                           kind_type,
                           scorepad,
                           ):

    final_dice = sorted(final_dice)

    check_dice = np.array(final_dice)
    print(f'numpy test: {check_dice}')

    (unique, counts) = np.unique(check_dice, return_counts=True)
    check_counts = np.asarray((unique, counts)).T
    value_counts = []
    for _ in check_counts:
        value_counts.append(_[1])

    if kind_type == 3 and kind_type in value_counts:
        return sum(final_dice)
    elif kind_type == 4 and kind_type in value_counts:
        return sum(final_dice)
    elif kind_type == 5 and kind_type in value_counts:
        return fixed_scores['score_kind_five_of']
    else:
        return 0


def score_full_house(final_dice,
                     scorepad,
                     ):

    final_dice = sorted(final_dice)

    check_full_house = np.array(final_dice)
    print(f'numpy test: {check_full_house}')

    (unique, counts) = np.unique(check_full_house, return_counts=True)
    check_counts = np.asarray((unique, counts)).T

    if check_counts[0][1] == 2 and check_counts[1][1] == 3 or check_counts[0][1] == 3 and check_counts[1][1] == 2:
        return fixed_scores['score_full_house']
    else:
        return 0


def score_small_straight(final_dice,
                         scorepad,
                         ):
    final_dice = sorted(final_dice)
    final_dice = final_dice[0:4]

    print(f'final dice: {final_dice}')

    small_straigh_list = [[1, 2, 3, 4,],
                          [2, 3, 4, 5,],
                          [3, 4, 5, 6,],
                          ]
    if final_dice in small_straigh_list:
        return fixed_scores['score_straight_small']
    else:
        return 0


def score_large_straight(final_dice,
                         scorepad,
                         ):
    if sorted(final_dice) in [[1, 2, 3, 4, 5],
                              [2, 3, 4, 5, 6],
                              ]:
        return fixed_scores['score_straight_large']
    else:
        return 0


def score_chance(final_dice,
                 scorepad,
                 ):
    return sum(final_dice)


def validate_bonus(scorepad):  #  Need to add code to validate
    """Need to check if bonus scoring is valid.
    Bonus is awarded when there has already been one five of a kind and there
    are still at least one category that has not yet been scored.
    """
    return True


def process_category_selection(final_dice, selection, scorepad):
    """Based on selection from user calculate and populate scorepad object with
    score and return object"""

    # Update score for selection of 1's through 6's
    if selection in ['1',
                     '2',
                     '3',
                     '4',
                     '5',
                     '6',
                     ]:

        upper_score = upper_section_score(int(selection),
                                          final_dice,
                                          scorepad,
                                          )

        if selection == '1':
            scorepad.upper_ones += upper_score
            scorepad.track_ones = 1
        elif selection == '2':
            scorepad.upper_twos += upper_score
            scorepad.track_twos = 1
        elif selection == '3':
            scorepad.upper_threes += upper_score
            scorepad.track_threes = 1
        elif selection == '4':
            scorepad.upper_fours += upper_score
            scorepad.track_fours = 1
        elif selection == '5':
            scorepad.upper_fives += upper_score
            scorepad.track_fives = 1
        elif selection == '6':
            scorepad.upper_sixes += upper_score
            scorepad.track_sixes = 1
        else:
            print('*** ERROR - INVALID UPPER SECTION SELECTION ***')

        if scorepad.lower_full_house != 0:
            scorepad.track_full_house = 1

    if selection == 'A':  # Three of a Kind
        scorepad.lower_kind_three_of = score_number_of_a_kind(final_dice,
                                                              3,
                                                              scorepad,
                                                              )
        scorepad.track_kind_three_of = 1
        if scorepad.lower_full_house != 0:
            scorepad.track_full_house = 1

    if selection == 'B':  # Four of a Kind
        scorepad.lower_kind_four_of = score_number_of_a_kind(final_dice,
                                                             4,
                                                             scorepad,
                                                             )
        scorepad.track_kind_four_of = 1
        if scorepad.lower_full_house != 0:
            scorepad.track_full_house = 1

    if selection == 'C':  # Full House
        scorepad.lower_full_house = score_full_house(final_dice,
                                                     scorepad,
                                                     )
        if scorepad.lower_full_house != 0:
            scorepad.track_full_house = 1

    if selection == 'D':  # Small Straight
        scorepad.lower_straight_small = score_small_straight(final_dice,
                                                             scorepad,
                                                             )
        scorepad.track_straight_small = 1

    if selection == 'E':  # Large Straight
        scorepad.lower_straight_large = score_large_straight(final_dice,
                                                             scorepad,
                                                             )
        scorepad.track_straight_large = 1

    if selection == 'F':  # Five of a Kind
        scorepad.lower_kind_five_of = score_number_of_a_kind(final_dice,
                                                             5,
                                                             scorepad,
                                                             )
        scorepad.track_kind_five_of = 1

    if selection == 'G':  # Total all dice
        scorepad.lower_all_dice = score_chance(final_dice,
                                               scorepad,
                                               )
        scorepad.track_all_dice = 1

    if selection == 'H':  # Bonus for additional Five of a Kind
        if scorepad.track_kind_five_of == 1 and validate_bonus(scorepad):
            scorepad.lower_bonus += 100
            scorepad.track_bonus += 1

    return scorepad


if __name__ == '__main__':

    # Create function test of scoring system  #TODO
    #
    #  TODO

    import sys

    print('Running as __main__')

    for _ in sys.path:
        print(_)
    print('=' * 50)

    from .. scorekeeping.scorepad import Scorepad_

    score_keep = Scorepad_('Player')

    print(f'{score_keep.name}')

    # final_dice = [1, 1, 1, 3, 1]
    # selection = '1'

    final_dice = [3, 5, 3, 3, 5]
    selection = 'c'


    score_keep = process_category_selection(final_dice,
                                            selection.upper(),
                                            score_keep,
                                            )
    print(f'final dice list: {final_dice}')
    print(f'score_keep.upper_ones = {score_keep.upper_ones}')
    print(f'score_keep.track_ones = {score_keep.track_ones}')
    print(f'score_keep.upper_twos = {score_keep.upper_twos}')
    print(f'score_keep.track_twos = {score_keep.track_twos}')
    print(f'score_keep.upper_threes = {score_keep.upper_threes}')
    print(f'score_keep.track_threes = {score_keep.track_threes}')
    print(f'score_keep.lower_full_house = {score_keep.lower_full_house}')
    print(f'score_keep.track_track_full_house = {score_keep.track_full_house}')
