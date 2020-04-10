"""Test scoring process"""

import sys
from .. scorekeeping.scorepad import Scorepad_
from .. gameprocessing.scoring import process_category_selection

# Selection choices list

selection_choices = ['1',
                     '2',
                     '3',
                     '4',
                     '5',
                     '6',
                     'a',
                     'b',
                     'c',
                     'd',
                     'e',
                     'f',
                     'g',
                     'h',
                     ]

# Final Dice samples by category
"""dict setup for sample dice
    pass/fail: test type to confirm pass or a fail
    category description
    dice roll : list of five ints between 1 and 6
    expected score
    tracking flag : 1 - score applied, 0 - score not applied
    object attribute name : from Scorepad_ Class - score
    object attribute name : from Scorepad_ Class - tracking flag
    selection menu item : choice entered by user
"""

sample_dice = {'pass': {'ones': [[1, 2, 1, 5, 1], 3, 1, 'upper_ones', 'track_ones', '1'],
                        'twos': [[4, 2, 1, 2, 1], 4, 1, 'upper_twos', 'track_twos', '2'],
                        'threes': [[3, 3, 1, 5, 3], 9, 1, 'upper_threes', 'track_threes', '3'],
                        'fours': [[1, 2, 1, 5, 1], 3, 1, 'upper_fours', 'track_fours', '4'],
                        'fives': [[5, 3, 1, 5, 1], 10, 1, 'upper_fives', 'track_fives', '5'],
                        'sixes': [[6, 2, 6, 5, 3], 12, 1, 'upper_sixes', 'track_sixes', '6'],
                        'three_of_a_kind': [[1, 2, 1, 5, 1], 10, 1, 'lower_kind_three_of', 'track_kind_three_of', 'a'],
                        'four_of_a_kind': [[5, 5, 2, 5, 5], 22, 1, 'lower_kind_four_of', 'track_kind_four_of', 'b'],
                        'full_house': [[1, 2, 1, 2, 1], 25, 1, 'lower_full_house', 'track_full_house', 'c'],
                        'small_straight': [[2, 3, 4, 5, 4], 30, 1, 'lower_straight_small', 'track_straight_small', 'd'],  # Observe
                        'large_straight': [[1, 2, 3, 4, 5], 40, 1, 'lower_straight_large', 'track_straight_large', 'e'],
                        'five_of_a_kind': [[3, 3, 3, 3, 3], 50, 1, 'lower_kind_five_of', 'track_kind_five_of', 'f'],
                        'any_dice': [[3, 3, 1, 2, 5], 14, 1, 'lower_all_dice', 'track_all_dice', 'g'],
                        'bonus': [[], 99, 1, 'lower_bonus', 'track_bonus', 'h']
                        },
               'fail': {'ones': [[3, 2, 2, 5, 1], 0, 0, 'upper_ones', 'track_ones', '1'],
                        'twos': [[1, 6, 1, 5, 1], 0, 0, 'upper_twos', 'track_twos', '2'],
                        'threes': [[1, 2, 1, 5, 1], 0, 0, 'upper_threes', 'track_threes', '3'],
                        'fours': [[1, 2, 1, 5, 1], 0, 0, 'upper_fours', 'track_fours', '4'],
                        'fives': [[1, 2, 3, 4, 1], 0, 0, 'upper_fives', 'track_fives', '5'],
                        'sixes': [[4, 2, 1, 5, 1], 0, 0, 'upper_sixes', 'track_sixes', '6'],
                        'three_of_a_kind': [[1, 2, 6, 5, 1], 0, 0, 'lower_kind_three_of', 'track_kind_three_of', 'a'],
                        'four_of_a_kind': [[1, 3, 1, 5, 1], 0, 0, 'lower_kind_four_of', 'track_kind_four_of', 'b'],
                        'full_house': [[1, 2, 4, 6, 1], 0, 0, 'lower_full_house', 'track_full_house', 'c'],
                        'small_straight': [[1, 2, 3, 5, 3], 0, 0, 'lower_straight_small', 'track_straight_small', 'd'],
                        'large_straight': [[1, 2, 3, 4, 6], 0, 0, 'lower_straight_large', 'track_straight_large', 'e'],
                        'five_of_a_kind': [[3, 2, 1, 5, 4], 0, 0, 'lower_kind_five_of', 'track_kind_five_of', 'f'],
                        'any_dice': [[4, 3, 1, 6, 1], 15, 0, 'lower_all_dice', 'track_all_dice', 'g'],
                        'bonus': [[], 99, 0, 'lower_bonus', 'track_bonus', 'h']
                        },
               }

# Test with pytest


def test_full_house():
    score_test = Scorepad_('Tester')
    final_dice = [3, 5, 3, 3, 5]
    selection = 'c'

    score_test = process_category_selection(final_dice,
                                            selection.upper(),
                                            score_test,
                                            )

    assert score_test.lower_full_house == 25 and score_test.track_full_house == 1


def test_full_house_fail():
    score_test = Scorepad_('Tester')
    final_dice = [3, 5, 3, 1, 5]
    selection = 'c'

    score_test = process_category_selection(final_dice,
                                            selection.upper(),
                                            score_test,
                                            )

    assert score_test.lower_full_house == 0 and score_test.track_full_house == 0


def test_full_house2():
    score_test = Scorepad_('Tester')
    score_check = ['lower_full_house',
                   'score_test.lower_kind_three_of',
                   ]

    # final_dice = [3, 5, 3, 3, 5]
    # selection = 'c'

    score_test = process_category_selection(sample_dice['pass']['full_house'][0],
                                            selection_choices[8].upper(),
                                            score_test,
                                            )

    # assert score_test.lower_full_house == sample_dice['pass']['full_house'][1] and score_test.track_full_house == sample_dice['pass']['full_house'][2]

    # assert score_test.lower_full_house == sample_dice['pass']['full_house'][1] and score_test.track_full_house == sample_dice['pass']['full_house'][2]

    assert getattr(score_test, sample_dice['pass']['full_house'][3]) == sample_dice['pass']['full_house'][1] and score_test.track_full_house == sample_dice['pass']['full_house'][2]


def test_all():
    """Iterate through all possible selection choices and test expected values
    """
    score_test = Scorepad_('Tester')

    for _ in sample_dice['pass'].values():

        score_test = process_category_selection(_[0],
                                                _[5].upper(),
                                                score_test,
                                                )

        assert getattr(score_test, _[3]) == _[1] and getattr(score_test, _[4]) == _[2]


        # [[3, 3, 1, 5, 3], 9, 1, 'upper_threes', 'track_threes', '3']

        # process_category_selection(final_dice, selection, scorepad):

        # sample_dice = {'pass': {'ones': [[1, 2, 1, 5, 1], 3, 1, 'upper_ones', 'track_ones', '1'],

