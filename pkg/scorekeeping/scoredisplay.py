"""Display current score using the scorepad object"""

from .. scorekeeping.scorepad import Scorepad_


def show_current_score(scorepad,
                       upper_section_total,
                       upper_section_bonus_calc,
                       upper_section_total_and_bonus,
                       lower_section_total,
                       grand_total,
                       ):

    print('===============================================')
    print('*** UPPER SECTION ***')
    print('-----------------------------------------------')
    print(f'One\'s:   {scorepad.upper_ones:3d}    ', end='')
    print(f'Two\'s:    {scorepad.upper_twos:2d}     ', end='')
    print(f'Three\'s:  {scorepad.upper_threes:3d}')
    print()
    print(f'Four\'s:  {scorepad.upper_fours:3d}    ', end='')
    print(f'Five\'s:   {scorepad.upper_fives:2d}     ', end='')
    print(f'Six\'s:    {scorepad.upper_sixes:3d}')
    print('-----------------------------------------------')
    print(f'Total Score:  {upper_section_total:3d}      ', end='')
    print(f'Bonus:  {upper_section_bonus_calc}')
    print('-----------------------------------------------')
    print(f'Upper Total:  {upper_section_total_and_bonus:3d}')
    print('===============================================')
    print('*** LOWER SECTION ***')
    print('-----------------------------------------------')
    print(f'Three of a Kind: {scorepad.lower_kind_three_of:3d}      ', end='')
    print(f'Four of a Kind: {scorepad.lower_kind_four_of:3d}')
    print()
    print(f'Full House:      {scorepad.lower_full_house:3d}')
    print()
    print(f'Small Straight:  {scorepad.lower_straight_small:3d}      ', end='')
    print(f'Large Straight: {scorepad.lower_straight_large:3d}')
    print()
    print(f'Five of a Kind:  {scorepad.lower_kind_five_of:3d}      ', end='')
    print(f'Any Dice:       {scorepad.lower_all_dice:3d}')
    print('-----------------------------------------------')
    print(f'Five of a Kind Bonus     ', end='')
    print(f' Count:{scorepad.lower_bonus_count:2d}', end='')
    print(f' Score: {scorepad.lower_bonus:3d}')
    print('===============================================')

    print(f'Lower Total:  {lower_section_total:3d}         ', end='')
    print(f'Upper Total:  {upper_section_total_and_bonus:5d}')
    print('-----------------------------------------------')
    print(f'Grand Total:  {grand_total}')
    print('===============================================')


if __name__ == '__main__':
    """Test score display and formatting"""
    scorepad = Scorepad_('Test-Display')

    scorepad.upper_ones = 6
    scorepad.upper_twos = 12
    scorepad.upper_threes = 18
    scorepad.upper_fours = 24
    scorepad.upper_fives = 30
    scorepad.upper_sixes = 36
    scorepad.lower_kind_three_of = 20
    scorepad.lower_kind_four_of = 10
    scorepad.lower_full_house = 25
    scorepad.lower_straight_small = 30
    scorepad.lower_straight_large = 40
    scorepad.lower_kind_five_of = 50
    scorepad.lower_all_dice = 6
    scorepad.lower_bonus_count = 1
    scorepad.lower_bonus = 100

    xxx = scorepad.upper_section_total()
    show_current_score(scorepad,
                       scorepad.upper_section_total(),
                       scorepad.upper_section_bonus_calc(),
                       scorepad.upper_section_total_and_bonus(),
                       scorepad.lower_section_total(),
                       scorepad.grand_total(),
                       )
