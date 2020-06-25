"""Calculate score for all categories"""

import numpy as np

from . menu import scorepad_available_scores

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

    (unique, counts) = np.unique(check_dice, return_counts=True)
    check_counts = np.asarray((unique, counts)).T
    value_counts = []

    for _ in check_counts:
        value_counts.append(_[1])

    if kind_type == 3 and (kind_type in value_counts or (kind_type + 1 or kind_type + 2) in value_counts):
        return sum(final_dice)
    elif kind_type == 4 and (kind_type in value_counts or kind_type + 1 in value_counts):
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

    (unique, counts) = np.unique(check_full_house, return_counts=True)
    check_counts = np.asarray((unique, counts)).T

    if check_counts[0][1] == 2 and check_counts[1][1] == 3 or check_counts[0][1] == 3 and check_counts[1][1] == 2:
        return fixed_scores['score_full_house']
    else:
        return 0


def score_small_straight(final_dice,
                         scorepad,
                         ):

    final_dice = set(final_dice)
    final_dice = str(sorted(final_dice)).strip('[]')

    small_straigh_list = [[1, 2, 3, 4,],
                          [2, 3, 4, 5,],
                          [3, 4, 5, 6,],
                          ]

    confirm_small_straight = False

    for _ in small_straigh_list:
        if str(_).strip('[]') in final_dice:
            confirm_small_straight = True
            break

    if confirm_small_straight:
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


def validate_bonus(scorepad):
    """Need to check if bonus scoring is valid.
    Bonus is awarded when there has already been one five of a kind and there
    are still at least one category that has not yet been scored.
    """
    score_tracking = scorepad_available_scores(scorepad)

    print(f'********** len(score_tracking["AVAILABLE"]: {len(score_tracking["AVAILABLE"])}')

    if len(score_tracking["AVAILABLE"]) > 0 and scorepad.lower_kind_five_of == 50:
        return True
    else:
        return False


def process_category_selection(final_dice,
                               selection,
                               scorepad
                               ):
    """Based on selection from user calculate and populate scorepad object with
    score and return object"""

    selection = selection.upper()  # convert selection to uppercase

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

        if selection == '1' and scorepad.track_ones == 0:
            scorepad.upper_ones += upper_score
            scorepad.track_ones = 1
            if upper_score == 0:
                scorepad.zeroed_ones = '*'

        elif selection == '2' and scorepad.track_twos == 0:
            scorepad.upper_twos += upper_score
            scorepad.track_twos = 1
            if upper_score == 0:
                scorepad.zeroed_twos = '*'

        elif selection == '3' and scorepad.track_threes == 0:
            scorepad.upper_threes += upper_score
            scorepad.track_threes = 1
            if upper_score == 0:
                scorepad.zeroed_threes = '*'

        elif selection == '4' and scorepad.track_fours == 0:
            scorepad.upper_fours += upper_score
            scorepad.track_fours = 1
            if upper_score == 0:
                scorepad.zeroed_fours = '*'

        elif selection == '5' and scorepad.track_fives == 0:
            scorepad.upper_fives += upper_score
            scorepad.track_fives = 1
            if upper_score == 0:
                scorepad.zeroed_fives = '*'

        elif selection == '6' and scorepad.track_sixes == 0:
            scorepad.upper_sixes += upper_score
            scorepad.track_sixes = 1
            if upper_score == 0:
                scorepad.zeroed_sixes = '*'
        else:
            print('*** ERROR - INVALID UPPER SECTION SELECTION ***')

    # Three of a Kind
    if selection == 'A' and scorepad.track_kind_three_of == 0:
        scorepad.lower_kind_three_of = score_number_of_a_kind(final_dice,
                                                              3,
                                                              scorepad,
                                                              )
        scorepad.track_kind_three_of = 1
        if scorepad.lower_kind_three_of == 0:
            scorepad.zeroed_kind_three_of = '*'

    # Four of a Kind
    if selection == 'B' and scorepad.track_kind_four_of == 0:
        scorepad.lower_kind_four_of = score_number_of_a_kind(final_dice,
                                                             4,
                                                             scorepad,
                                                             )
        scorepad.track_kind_four_of = 1
        if scorepad.lower_kind_four_of == 0:
            scorepad.zeroed_kind_four_of = '*'

    # Full House
    if selection == 'C' and scorepad.track_full_house == 0:
        scorepad.lower_full_house = score_full_house(final_dice,
                                                     scorepad,
                                                     )
        scorepad.track_full_house = 1
        if scorepad.lower_full_house == 0:
            scorepad.zeroed_full_house = '*'

    # Small Straight
    if selection == 'D' and scorepad.track_straight_small == 0:
        scorepad.lower_straight_small = score_small_straight(final_dice,
                                                             scorepad,
                                                             )
        scorepad.track_straight_small = 1
        if scorepad.lower_straight_small == 0:
            scorepad.zeroed_straight_small = '*'

    # Large Straight
    if selection == 'E' and scorepad.track_straight_large == 0:
        scorepad.lower_straight_large = score_large_straight(final_dice,
                                                             scorepad,
                                                             )
        scorepad.track_straight_large = 1
        if scorepad.lower_straight_large == 0:
            scorepad.zeroed_straight_large = '*'

    # Five of a Kind
    if selection == 'F' and scorepad.track_kind_five_of == 0:
        scorepad.lower_kind_five_of = score_number_of_a_kind(final_dice,
                                                             5,
                                                             scorepad,
                                                             )
        scorepad.track_kind_five_of = 1
        if scorepad.lower_kind_five_of == 0:
            scorepad.zeroed_kind_five_of = '*'

    # Total all dice
    if selection == 'G' and scorepad.track_all_dice == 0:
        scorepad.lower_all_dice = score_chance(final_dice,
                                               scorepad,
                                               )
        scorepad.track_all_dice = 1
        if scorepad.lower_all_dice == 0:
            scorepad.zeroed_all_dice = '*'

    # Bonus for additional Five of a Kind
    if selection == 'H':
        # Confirm dice are five of a kind
        if score_number_of_a_kind(final_dice,
                                  5,
                                  scorepad,
                                  ) == 50:

            if scorepad.track_kind_five_of == 1 and validate_bonus(scorepad):
                scorepad.lower_bonus += 100
                scorepad.lower_bonus_count += 1
                return scorepad
    return scorepad


if __name__ == '__main__':

    # Test code. See test package for pytest funcitonal tests.

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

    score_keep.bonus_counter = 1
    score_keep.lower_bonus = 100
    score_keep.track_kind_five_of = 1
    score_keep.lower_kind_five_of = 50
    final_dice = [4, 4, 4, 4, 4]
    selection = 'h'

    score_keep = process_category_selection(final_dice,
                                            selection.upper(),
                                            score_keep,
                                            )

    print(f'scorepad.track_kind_five_of: {score_keep.track_kind_five_of}')

    print(f'score_keep.lower_kind_five_of : {score_keep.lower_kind_five_of}')
    print(f'selection; {selection}')
    print(f'final dice list: {final_dice}')

    print(score_number_of_a_kind(final_dice,
                                 5,
                                 score_keep,
                                 ))


    print(f'score_keep.lower_bonus : {score_keep.lower_bonus}')
    print(f'score_keep.bonus_counter : {score_keep.bonus_counter}')


    # print(f'score_keep.lower_straight_small = {score_keep.lower_straight_small}')

    score_number_of_a_kind

    # print(f'score_keep.upper_ones = {score_keep.upper_ones}')
    # print(f'score_keep.track_ones = {score_keep.track_ones}')
    # print(f'score_keep.upper_twos = {score_keep.upper_twos}')
    # print(f'score_keep.track_twos = {score_keep.track_twos}')
    # print(f'score_keep.upper_threes = {score_keep.upper_threes}')
    # print(f'score_keep.track_threes = {score_keep.track_threes}')
    # print(f'score_keep.lower_full_house = {score_keep.lower_full_house}')
    # print(f'score_keep.track_track_full_house = {score_keep.track_full_house}')
