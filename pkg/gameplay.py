"""Process game play"""

from diceroll.dice import die_roll

if __name__ == '__main__':

    # Lists to store initial rolls and final dice

    dice_roll = []
    final_dice = []
    new_dice = 0

    # Three rolls per turn

    for roll in range(1, 4):
        print(f'roll: {roll}')
        if roll == 1:
            for initial in range(1, 6):
                dice_roll.append(die_roll())
        else:
            for next_roll in range(1, (new_dice + 1)):
                dice_roll.append(die_roll())

        print(f'rolled dice: {dice_roll}')
        dice_roll = []
        new_dice = int(input('How many dice to roll? '))

