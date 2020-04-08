"""Workflow for a player's turn at rollling the dice"""

from diceroll.dice import die_roll
from diceroll.dicegraphic import dice_display

# Lists to store initial rolls and final dice

dice_roll = []
dice_list_hold = []
dice_list_hold_idx = []
final_dice = []
new_dice_qty = 0


def request_dice_to_keep():
    print('Enter dice to keep. "Q" to keep all dice and quit turn.')
    dice_list_hold_idx = input('Dice to keep?: ')
    if dice_list_hold_idx[0].upper() == 'Q':
        print('Quitting turn...')
    return dice_list_hold_idx


def store_dice_to_keep(dice_list_hold_idx, dice_roll):
    dice_list_hold = []

    if dice_list_hold_idx[0].upper() == 'Q':
        return dice_list_hold

    for hold in dice_list_hold_idx:
        dice_list_hold.append(dice_roll[int(hold) - 1])
    return dice_list_hold


def get_and_store_dice_to_keep(dice_roll):
    dice_list_hold_idx = request_dice_to_keep()
    dice_list_hold = store_dice_to_keep(dice_list_hold_idx, dice_roll)
    return (dice_list_hold_idx,
            dice_list_hold,
            )


if __name__ == '__main__':

    """This section generates the dice rolls and gets the dice the player
    wants to keep before the next rolls. Will need to set up as a function
    in possibly another module. Will also need to determine if there are
    additional sections that can be put into a function to reduce repitiion.
    """

    # Player turn
    # Three rolls per turn

    # Roll One - roll all five dice

    print('First Roll:')

    # First roll is all five dice
    for roll1 in range(1, 6):
        dice_roll.append(die_roll())

    # Show dice
    dice_roll = sorted(dice_roll)
    dice_display(dice_roll)

    # Get dice to keep and store for next roll
    (dice_list_hold_idx,
     dice_list_hold,
     ) = get_and_store_dice_to_keep(dice_roll)

    # Proceed to second roll if not quitting turn after first roll
    if dice_list_hold_idx[0].upper() != 'Q':

        # reset for next dice roll
        dice_roll = []

        # Roll Two - roll dice not kept

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

        # Show dice
        dice_roll = sorted(dice_roll)
        dice_display(dice_roll)

    if dice_list_hold_idx[0].upper() != 'Q':
        # Roll Three - roll dice not kept

        # Clear dice previously held and request new dice to keep
        dice_list_hold = []

        (dice_list_hold_idx,
         dice_list_hold,
         ) = get_and_store_dice_to_keep(dice_roll)

        # Proceed to third roll if not quitting turn after second roll
        if dice_list_hold_idx[0].upper() != 'Q':

            # reset for next dice roll
            dice_roll = []

            print()
            print('Third Roll:')

            new_dice_qty = 5 - len(dice_list_hold)

            # Add dice that were kept to the new set of dice
            for keep_die in dice_list_hold:
                dice_roll.append(int(keep_die))

            for next_roll in range(1, (new_dice_qty + 1)):
                dice_roll.append(die_roll())

            # Show dice
            dice_roll = sorted(dice_roll)
            dice_display(dice_roll)

    final_dice = dice_roll
    print('*** End Turn ***')

    # Show dice being held for scoring
    print()
    print('Here are the dice to be scored:')
    print()
    dice_display(final_dice)
    print()
    print('Proceed to scoring...')
