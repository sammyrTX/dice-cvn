"""Store scores for players"""

# Points for fixed score categories in Dict

fixed_scores = {'score_full_house': 25,
                'score_straight_small': 30,
                'score_straight_large': 40,
                'score_kind_five_of': 50,
                'upper_section_bonus': 35,
                }

# Lower section categories that use total of dice for score

lower_section_categories_total_dice_score = ['lower_kind_three_of',
                                             'lower_kind_four_of',
                                             'lower_all_dice',
                                             ]


class Scorepad_:
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
        self.lower_bonus_count = 0
        self.lower_bonus = 0
        self.track_ones = 0
        self.track_twos = 0
        self.track_threes = 0
        self.track_fours = 0
        self.track_fives = 0
        self.track_sixes = 0
        self.track_kind_three_of = 0
        self.track_kind_four_of = 0
        self.track_full_house = 0
        self.track_straight_small = 0
        self.track_straight_large = 0
        self.track_kind_five_of = 0
        self.track_all_dice = 0
        self.upper_section_total_show = self.upper_section_total()
        self.available_choices = self.initialize_choices_list()
        self.web_turn_tracking = 0
        self.web_dice_list = []
        self.web_dice_list_hold = []

    def __repr__(self):
        return repr(f'Player name ***: {self.name}')

    def upper_section_bonus_calc(self):

        if self.upper_section_total() >= 63:
            return fixed_scores['upper_section_bonus']
        else:
            return 0

    def upper_section_total(self):
        upper_section = [self.upper_ones,
                         self.upper_twos,
                         self.upper_threes,
                         self.upper_fours,
                         self.upper_fives,
                         self.upper_sixes,
                         ]

        return sum(upper_section)

    def upper_section_total_and_bonus(self):

        return self.upper_section_total() + self.upper_section_bonus_calc()

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
        return self.upper_section_total_and_bonus() + self.lower_section_total()

    def initialize_choices_list(self):
        """Returns a list of choices that are availble and as player makes a
        selection during the game, the choice is removed from this list.
        """

        return ['1',  # Ones
                '2',  # Twos
                '3',  # Threes
                '4',  # Fours
                '5',  # Fives
                '6',  # Sixes
                'A',  # Three of a Kind
                'B',  # Four of a Kind
                'C',  # Full House
                'D',  # Small Straight
                'E',  # Large Straight
                'F',  # Five of a Kind
                'G',  # Any Dice
                'H',  # Five of a Kind Bonus
                ]


def total_all_dice(dice_list):
    return sum(dice_list)


def upper_section_scoring(die_value, dice_list):

    score = 0
    print(f'die value: {die_value}')

    for _ in dice_list:
        if _ == die_value:
            score += die_value

    return score


def lower_section_scoring(score_category, dice_list):
    if score_category in lower_section_categories_total_dice_score:
        return total_all_dice(dice_list)
    else:
        return fixed_scores[score_category]


if __name__ == '__main__':
    ###############################################################################
    # Object Testing

    player1 = Scorepad_('Johnny')

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
    player1.lower_full_house += lower_section_scoring('score_full_house',
                                                      test_list
                                                      )

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
    print()
    print(f"Full House Score: {fixed_scores['score_full_house']}")
    print(f"Small Straight Score: {fixed_scores['score_straight_small']}")
    print(player1)
