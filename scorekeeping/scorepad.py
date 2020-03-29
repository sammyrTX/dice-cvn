"""Store scores for players"""

# Set points for fixed score categories

score_full_house = 25
score_straight_small = 30
score_straight_large = 40
score_kind_five_of = 50


class scorepad_:
    """Store player score for each category"""
    def __init__(self,
                 name,
                 ):
        self.name = name
        self.upper_ones = 0
        self.upper_twos = 0
        self.upper_threes = 0
        self.upper_fours = 0
        self.upper_fives = 0
        self.upper_sixes = 0
        self.lower_kind_three_of = 0
        self.lower_kind_four_of = 0
        self.lower_full_house = 0
        self.lower_straight_small = 0
        self.lower_straight_large = 0
        self.lower_kind_five_of = 0
        self.lower_all_dice = 0
        self.lower_bonus = 0

    def __repr__(self):
        return repr(f'Player name ***: {self.name}')

    def upper_section_total(self):
        upper_section = [self.upper_ones,
                         self.upper_twos,
                         self.upper_threes,
                         self.upper_fours,
                         self.upper_fives,
                         self.upper_sixes,
                         ]
        if sum(upper_section) >= 63:
            upper_bonus = 35
        else:
            upper_bonus = 0

        return sum(upper_section) + upper_bonus

    def lower_section_total(self):
        lower_section = [self.lower_kind_three_of,
                         self.lower_kind_four_of,
                         self.lower_full_house,
                         self.lower_straight_small,
                         self.lower_straight_large,
                         self.lower_kind_five_of,
                         self.lower_all_dice,
                         self.lower_bonus,
                         ]

        return sum(lower_section)

    def grand_total(self):
        return self.upper_section_total() + self.lower_section_total()


def total_all_dice(dice_list):
    return sum(dice_list)


def upper_section_scoring(die_value, dice_list):

    score = 0
    print(f'die value: {die_value}')

    for _ in dice_list:
        if _ == die_value:
            score += die_value

    return score






###############################################################################
# Object Testing

player1 = scorepad_('Johnny')

print(f'Name of player is {player1.name}')
print(f'Upper Section Scores:')
print(f'One\'s: {player1.upper_ones}')
print(f'Two\'s: {player1.upper_twos}')

test_list = [1, 1, 1, 4, 4, 3]

print()
print('Add 10 and 20 to each score respectively')

player1.upper_ones += 0
player1.upper_twos += 0
player1.upper_sixes += 0
player1.lower_full_house += 25
player1.lower_all_dice += total_all_dice(test_list)

player1.upper_ones += upper_section_scoring(5, test_list)

print(f'Updated Upper Section Scores:')
print(f'One\'s: {player1.upper_ones}')
print(f'Two\'s: {player1.upper_twos}')
print(f'Six\'s: {player1.upper_sixes}')
print(f'Full House: {player1.lower_full_house}')
print(f'Total All Dice: {player1.lower_all_dice}')
print()
print(f'Upper section total: {player1.upper_section_total()}')
print(f'Lower section total: {player1.lower_section_total()}')
print(f'Grand total: {player1.grand_total()}')
print(player1)
