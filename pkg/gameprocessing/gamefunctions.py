"""Game functions to process game play, scoring, etc."""


# Points for fixed score categories in Dict

fixed_scores = {'score_full_house': 25,
                'score_straight_small': 30,
                'score_straight_large': 40,
                'score_kind_five_of': 50,
                'upper_section_bonus': 35,
                }

def upper_section_score(die_value, final_dice):
    """Evaluate dice from a roll for a given value and multiply the count
    by that value. E.g. for a die value of 3 and a count of two dice with
    that value the total score is 6 (die value of 3 times a count of two)
    """
    return final_dice.count(die_value) * die_value

# Review scoring process for small straight  #TODO


def score_three_of_a_kind(final_dice):
    pass


def score_four_of_a_kind(final_dice):
    pass


def score_full_house(final_dice):
    pass


def score_small_straight(final_dice):
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


def score_large_straight(final_dice):
    if sorted(final_dice) in [[1, 2, 3, 4, 5],
                              [2, 3, 4, 5, 6],
                              ]:
        print('it is a large straight')
        return fixed_scores['score_straight_large']
    else:
        return 0


if __name__ == '__main__':

    pass_this_list = [1, 1, 3, 4, 1, 2, 3, 3, 3,]
    die_value = int(input('Enter a value to count in the list: '))
    print(f'Count of {die_value}s in a list ({pass_this_list}) : {pass_this_list.count(die_value)}')
    print(f'Score is {upper_section_score(die_value, pass_this_list)}')

    pass_this_small_straight = [1, 2, 3, 4, 6]

    pass_this_large_straight = [1, 2, 3, 4, 5]

    print(f'Score this roll: {pass_this_small_straight}')
    print(f'Score: {score_small_straight(pass_this_small_straight)}')

    print(f'Score this roll: {pass_this_small_straight}')
    print(f'Score: {score_small_straight(pass_this_small_straight)}')
    print()
    print(f'Score this roll: {pass_this_large_straight}')
    print(f'Score: {score_large_straight(pass_this_large_straight)}')
