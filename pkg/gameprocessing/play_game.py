"""Module for game play"""

import os
from . player_turn import player_turn
from . menu import scorepad_available_scores

from .. scorekeeping.scorepad import Scorepad_
from .. scorekeeping.scoredisplay import show_current_score


def game_status(scorepad):
    """Check score categories to determine if player has used up all available
    scores. Return True to continue playing or False to complete game.
    """

    score_status = scorepad_available_scores(scorepad)

    # Determine if there are available scores in order to conutune rolling
    # If there is at least one category left return True else False
    if len(score_status['AVAILABLE']) > 0:
        return True
    else:
        return False


def start_game():
    """Main function to initiate and handle entire game."""

    # Request player name and instantiate scorepad_ object
    scorepad = Scorepad_('Player01')

    while True:

        while True:
            scorepad = player_turn(scorepad)
            os.system('clear')

            if game_status(scorepad):
                continue
            else:
                break
        break

    os.system('clear')

    print('Final Score:')

    show_current_score(scorepad,
                       scorepad.upper_section_total(),
                       scorepad.upper_section_bonus_calc(),
                       scorepad.upper_section_total_and_bonus(),
                       scorepad.lower_section_total(),
                       scorepad.grand_total(),
                       )
    print()
    print(f'Thanks for playing! Your final score is {scorepad.grand_total()}')
    print()


if __name__ == '__main__':

    start_game()

    print('* GAME OVER *')

    # Name input needs to be either in a main starting point module or
    # as a mini function

    # Request player name and instanciate scorepad_ object
    # scorepad = Scorepad_(input('Please enter your name: '))
    # print(f'Let\'s start, {scorepad.name}...')

    # game_status(scorepad)  # test game_status function

    # while True:

    #     player_turn(scorepad)
    #     input('Press enter to continue')
    #     break

    # print('*** Ready for next turn ***')
