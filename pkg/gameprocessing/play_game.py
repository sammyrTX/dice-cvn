"""Module for game play"""

import os
from . player_turn import player_turn
from . menu import scorepad_available_scores

from .. scorekeeping.scorepad import Scorepad_


def game_status(scorepad):
    """Check score categories to determine if player has used up all available
    scores. Return True to continue playing or False to complete game.
    """

    score_status = scorepad_available_scores(scorepad)

    # Determine if there are available scores in order to conutune rolling
    # If there is at least one category left return True else False
    if len(score_status) > 0:
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
