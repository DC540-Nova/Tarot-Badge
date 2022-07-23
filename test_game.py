# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
# Developer: Corinne "Rinn" Neidig
#
# Copyright (c) 2022 DC540 Defcon Group
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# UNITTEST
# --------
# import unittest
# unittest.main('test_game')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from config import BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display, neo_pixel, \
    nrf
from encryption import Encryption
from touch import Touch
from file_manager import FileManager
from demo import Demo
from tarot import Tarot
from game import Game
from morse_code import MorseCode
import data

encryption = Encryption()
touch = Touch(BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display)
file_manager = FileManager(touch, display, neo_pixel)
tarot = Tarot(touch, display, data.cards)
morse_code = MorseCode(encryption, neo_pixel, neo_pixel.RED)


class TestGame(unittest.TestCase):
    """
    Test class to test game module
    """

    def setUp(self):
        """
        setUp class
        """
        # Init objects
        self.game = Game(touch, file_manager, display, tarot, morse_code)

    def tearDown(self):
        """
        tearDown class
        """
        pass

    # def test_multiple_choice_won(self):
    #     """
    #     test multiple_choice won functionality
    #
    #     Interactive Response:  [RANDOM MANUAL VALIDATION]
    #     """
    #     # Params
    #     question_bank = data.tarot_trivia_game
    #     game_number = '1'
    #     num_questions = 3
    #     num_questions_to_win = 2
    #     # Returns
    #     return_1 = '1 '
    #     # Calls
    #     won_game = self.game.multiple_choice(question_bank, game_number, num_questions, num_questions_to_win)
    #     if won_game:
    #         self.game.won(won_game)
    #     # Asserts
    #     self.assertEqual(won_game, return_1)
    #
    # def test_multiple_choice_lose(self):
    #     """
    #     test multiple_choice lose functionality
    #
    #     Interactive Response:  [RANDOM MANUAL VALIDATION]
    #     """
    #     # Params
    #     question_bank = data.tarot_trivia_game
    #     game_number = '1'
    #     num_questions = 3
    #     num_questions_to_win = 2
    #     # Returns
    #     return_1 = False
    #     # Calls
    #     won_game = self.game.multiple_choice(question_bank, game_number, num_questions, num_questions_to_win)
    #     if won_game:
    #         self.game.won(won_game)
    #     # Asserts
    #     self.assertEqual(won_game, return_1)

# TODO: practice unit test

    def test_morse_code_won(self):
        """
        test morse_code won functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        question_bank = data.morse_code_game
        game_number = '7'
        num_questions = 3
        num_questions_to_win = 3
        # Returns
        return_1 = '7 '
        # Calls
        won_game = self.game.morse_code_sequence(question_bank, game_number, num_questions, num_questions_to_win)
        if won_game:
            self.game.won(won_game)
        # Asserts
        self.assertEqual(won_game, return_1)

    # def test_question_loop_win_interactive(self):
    #     """
    #     test question_loop win functionality
    #
    #     Interactive Response:  60144559
    #     """
    #     # Setup
    #     str_status = '7 10 4 6 9 3 2 8 5 '
    #     file_manager.write_status_file(str_status)
    #     # Params
    #     question_number = '1'
    #     # Returns
    #     return_1 = None
    #     # Calls
    #     question = game.question_loop(question_number)
    #     # Asserts
    #     self.assertEqual(question, return_1)
    #

if __name__ == '__main__':
    unittest.main()