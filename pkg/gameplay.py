"""Process game play"""

from diceroll.dice import die_roll
from diceroll.dicegraphic import dice_display


def request_dice_to_keep():
    dice_list_hold_idx = input('Dice to keep?: ')
    print(f'{dice_list_hold_idx}')
    return dice_list_hold_idx


def store_dice_to_keep(dice_list_hold_idx, dice_roll):
    dice_list_hold = []
    for hold in dice_list_hold_idx:
        dice_list_hold.append(dice_roll[int(hold) - 1])
    return dice_list_hold


if __name__ == '__main__':

    # Lists to store initial rolls and final dice

    dice_roll = []
    dice_list_hold = []
    dice_list_hold_idx = []
    final_dice = []
    new_dice_qty = 0

    """This section generates the dice rolls and gets the dice the player
    wants to keep before the next rolls. Will need to set up as a function
    in possibly another module. Will also need to determine if there are
    additional sections that can be put into a function to reduce repitiion.
    """
    # Player turn
    # Three rolls per turn

    # Roll One - roll all five dice

    print('First Roll:')

    for roll1 in range(1, 6):
        dice_roll.append(die_roll())

    dice_roll = sorted(dice_roll)
    dice_display(dice_roll)

    dice_list_hold_idx = request_dice_to_keep()
    dice_list_hold = store_dice_to_keep(dice_list_hold_idx, dice_roll)

    dice_roll = []  # reset for next dice roll

    # Roll Two

    print()
    print('Second Roll:')

    # Get quantity of dice to roll next
    new_dice_qty = 5 - len(dice_list_hold)

    # Add dice that were kept to the new set of dice
    for keep_die in dice_list_hold:
        dice_roll.append(int(keep_die))

    # Roll dice that were not kept and add to the list
    for roll2 in range(1, (new_dice_qty + 1)):
        dice_roll.append(die_roll())

    dice_display(dice_roll)

    # Roll Three

    # Clear dice previously held and request new dice to keep
    dice_list_hold = []
    dice_list_hold_idx = request_dice_to_keep()
    dice_list_hold = store_dice_to_keep(dice_list_hold_idx, dice_roll)

    dice_roll = []  # reset for next dice roll

    print('Third Roll:')

    new_dice_qty = 5 - len(dice_list_hold)

    # Add dice that were kept to the new set of dice
    for keep_die in dice_list_hold:
        dice_roll.append(int(keep_die))

    for next_roll in range(1, (new_dice_qty + 1)):
        dice_roll.append(die_roll())

    dice_display(dice_roll)

    print('*** End Turn ***')
