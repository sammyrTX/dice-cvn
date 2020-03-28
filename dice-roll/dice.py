"""Functions to generate the roll of a six-sided die"""

from random import randint

# store dice results in a list
dice_list = []


def die_roll():
    """Generate a random number between 1 and 6"""
    die_result = randint(1, 6)
    # print(f'You rolled a {die_result}')

    return die_result


for _ in range(1, 6):

    dice_list.append(die_roll())

print(f'dice_list: {dice_list}')
