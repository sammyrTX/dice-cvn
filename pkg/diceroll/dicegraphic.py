"""Generate a text graphic of a die that can be displayed
horizontally by utilizing a list that can be iterated
"""

header = ['--1--',
          '--2--',
          '--3--',
          '--4--',
          '--5--',
          ]

dice_set = [
           ['-----',
            '|   |',
            '| O |',
            '|   |',
            '-----',
            ],
            ['-----',
             '|O  |',
             '|   |',
             '|  O|',
             '-----',
             ],
            ['-----',
             '|O  |',
             '| O |',
             '|  O|',
             '-----',
             ],
            ['-----',
             '|O O|',
             '|   |',
             '|O O|',
             '-----',
             ],
            ['-----',
             '|O O|',
             '| O |',
             '|O O|',
             '-----',
             ],
            ['-----',
             '|O O|',
             '|O O|',
             '|O O|',
             '-----',
             ],
             ]


def dice_display(dice_list):
    """For a given list of die values, generate a text graphic of the dice
    horizontally"""

    for die_position in range(5):
        pass
        print(f'{header[die_position]}' + ' ', end='  ')

    print()

    for _ in range(5):

        for dice in dice_list:
            print(f'{dice_set[dice - 1][_]}' + ' ', end='  ')

        print()


if __name__ == '__main__':

    test_list = [1,
                 6,
                 4,
                 5,
                 3,
                 ]

    print(f'Test set of dice values: {test_list}')
    print()

    dice_display(test_list)
