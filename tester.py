# Test module and packages

# from pkg.diceroll.dice import diceroll_dice_func

# from pkg.gameplay.gameplay import gameplay_gameplay_func

# print(f'dice.py: {diceroll_dice_func()}')
# print()
# print(f'gameplay.py: {gameplay_gameplay_func()}')

from random import randrange

# Generates a simple graphic of a die on the command line
r = randrange(6)
r = int(input('Enter number between 1 and 6: ')) - 1
C = 'o '
s = '-----\n|'+C[r < 1]+' '+C[r < 3]+'|\n|'+C[r < 5]

print(f'number: {r + 1}')
print(s+C[r & 1]+s[::-1])

print('+' * 45)
print('-----\n|')
print('+' * 45)
print(C[r < 1])
print('+' * 45)
print(' ')
print('+' * 45)
print(C[r < 3])
print('+' * 45)
print('|\n|')
print('+' * 45)
print(C[r < 5])
