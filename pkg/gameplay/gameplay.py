"""Process game play"""

import sys
try:
    from . import pkg
except ImportError:
    print('Package or Module not found error')


# print(f'sys.path: {sys.path}')

for _ in sys.path:
    print(_)

# sys.path.append(r'/mnt/MCRN_RAID1/work/PROJECTS/dice-cvn/diceroll')

# print(f'sys.path: {sys.path}')

print(dir())
print('*' * 60)
print()

# Testing - REMOVE BEFORE FLIGHT


def gameplay_gameplay_func():
    print('This is a function within gameplay.py')


if __name__ == '__main__':

    # Resume turn processing

    try:
        # from diceroll.dice import die_roll
        from .diceroll.dice import die_roll
        print(dir())
        # from .diceroll.dice import die_roll

    except ImportError:
        print('Module not found')

    # Lists to store initial rolls and final dice

    dice_roll = []
    final_dice = []
    new_dice = int

    # Three rolls per turn

    for roll in range(1, 4):
        print(f'roll: {roll}')
        if roll == 1:
            for initial in range(1, 6):
                dice_roll.append(die_roll())
        else:
            for next_roll in range(1, (new_dice + 1)):
                dice_roll.append(die_roll())

