# Test module and packages

from pkg.diceroll.dice import diceroll_dice_func

from pkg.gameplay.gameplay import gameplay_gameplay_func

print(f'dice.py: {diceroll_dice_func()}')
print()
print(f'gameplay.py: {gameplay_gameplay_func()}')
