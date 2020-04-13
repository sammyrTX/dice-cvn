"""Input player selection of score category to assign based on the
    dice held.
"""

# Valid Menu Item Keys
valid_keys = ['1',
              '2',
              '3',
              '4',
              '5',
              '6',
              'A',
              'B',
              'C',
              'D',
              'E',
              'F',
              'G',
              'H',
              ]

def get_player_selection():
    while True:
        user_choice = input('Please enter your choice by entering the menu item key: ')
        if user_choice.upper() in valid_keys:
            return user_choice
        else:
            print('Invalid item choice. Please try again.')



def process_category_selection(user_choice, scorepad):
    pass


if __name__ == '__main__':
    selection = get_player_selection()
    print()
    print(f'User entry is: {selection.upper()}')

