"""Functions to generate the roll of a six-sided die"""

from random import randint

# store dice results in a list
dice_list = []
dice_list_hold = []


def die_roll():
    """Generate a random number between 1 and 6"""

    die_result = randint(1, 6)

    return die_result


def show_dice(dice_list):
    for _ in enumerate(dice_list):
        print(f'die: {_[0] + 1} => {_[1]}')


def text_die(die_value):
    """Generate text rendering of a die for a given r"""
    pass
    C = 'o '
    s = '-----\n|' + C[die_value < 1] + ' ' + C[die_value < 3] + '|\n|' \
        + C[die_value < 5]

    print(s + C[die_value & 1] + s[::-1])


if __name__ == '__main__':

    # Code below generates a roll of five dice and then prompts user to
    # select dice to keep.

    for _ in range(1, 6):

        dice_list.append(die_roll())

    print(f'dice_list: {dice_list}')

    show_dice(dice_list)

    test_test = input('Enter a list: ')
    print(f'List entered: {test_test}')
    print('List using a for-loop:')

    # Use indexing below to select and collect die values for a given roll
    for items_ in test_test:
        idx = int(items_)
        print(f'die #: {items_}   value: {dice_list[idx - 1]}')
        dice_list_hold.append(dice_list[idx - 1])

    show_dice(dice_list_hold)
    print(f'Die values to keep: {dice_list_hold}')

    # **** Test generation of dice text
    # **** Need to next generate roll 2 and 3 and collect die rs

