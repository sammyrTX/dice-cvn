"""Functions to generate the roll of a six-sided die"""

# still need to resolve the sibling package import

import sys
from random import randint

sys.path.append('..')

for _ in sys.path:
    print(_)
print('=' * 50)

# import gameplay.gameplay

# from . pkg.gameplay import gameplay

# store dice results in a list
dice_list = []
dice_list_hold = []


def die_roll():
    """Generate a random number between 1 and 6"""
    die_result = randint(1, 6)
    # print(f'You rolled a {die_result}')

    return die_result

# Testing - REMOVE BEFORE FLIGHT


def diceroll_dice_func():
    print('This is a function within dice.py')


if __name__ == '__main__':

    sys.path.append('..')
    from pkg.gameplay import gameplay

    print('+' * 50)
    for x in sys.path:
        print(x)
    print('+' * 50)

    for _ in range(1, 6):

        dice_list.append(die_roll())

    print(f'dice_list: {dice_list}')

    for _ in enumerate(dice_list):
        print(f'die: {_[0] + 1}  value = {_[1]}')

    test_test = input('Enter a list: ')
    print(f'List entered: {test_test}')
    print('List using a for-loop:')

    # Use indexing below to select and collect die values for a given roll
    for items_ in test_test:
        # print(f'die #: {items_}')  #'   value: {dice_list[int(items_)]}')
        idx = int(items_)
        print(f'die #: {items_}   value: {dice_list[idx - 1]}')
        dice_list_hold.append(dice_list[idx - 1])

    print(f'Die values to keep: {dice_list_hold}')

    # **** Need to next generate roll 2 and 3 and collect die values

    # print(f'sys.path: {sys.path}')
    for _ in sys.path:
        print(_)

    # from gameplay.gameplay import gameplay_gameplay_func

    print(f'gameplay.py: {gameplay.gameplay_func()}')



