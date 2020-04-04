"""Process game play"""

from diceroll.dice import die_roll
from diceroll.dicegraphic import dice_display

if __name__ == '__main__':

    # Lists to store initial rolls and final dice

    dice_roll = []
    final_dice = []
    new_dice = 0

    # Player turn
    # Three rolls per turn

    # Roll One

    print('First Roll:')
    for initial in range(1, 6):
        dice_roll.append(die_roll())

    print(f'Result: *** {dice_roll} *** <<< REMOVE AFTER TESTING')
    dice_display(dice_roll)

    # Roll Two

    new_dice = int(input('How many dice to roll? '))
    dice_roll = []

    print('Second Roll:')
    for next_roll in range(1, (new_dice + 1)):
        dice_roll.append(die_roll())


    print(f'Result: *** {dice_roll} *** <<< REMOVE AFTER TESTING')
    dice_display(dice_roll)

    # Roll Three

    new_dice = int(input('How many dice to roll? '))
    dice_roll = []

    print('Third Roll:')
    for next_roll in range(1, (new_dice + 1)):
        dice_roll.append(die_roll())


    print(f'Result: *** {dice_roll} *** <<< REMOVE AFTER TESTING')
    dice_display(dice_roll)
