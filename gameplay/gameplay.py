"""Process game play"""

# Resume turn processing

from dice_roll.dice import die_roll

# Lists to store initial rolls and final dice

dice_roll = []
final_dice = []
new_dice = int

# Three rolls per turn

for roll in range(1, 4):
    print(f'roll: {roll}')
    if roll == 1:
        for initial in range(1, 6):
            dice_roll.add(die_roll())
    else:
        for next_roll in range(1, (new_dice + 1)):
            dice_roll.add(die_roll())


