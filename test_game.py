# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
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

from main import button_up, button_down, button_left, button_right, button_submit, button_extra, display, neo_pixel, nrf
from encryption import Encryption
from touch import Touch
from file_manager import FileManager
from demo import Demo
from tarot import Tarot
from game import Game
from morse_code import MorseCode
import data

encryption = Encryption()
touch = Touch(button_up, button_down, button_left, button_right, button_submit, button_extra, display)
file_manager = FileManager(touch, display, neo_pixel)
tarot = Tarot(file_manager, touch, display, nrf, neo_pixel, data.cards)
morse_code = MorseCode(encryption, neo_pixel, neo_pixel.RED)


class TestGame(unittest.TestCase):
    """
    Test class to test game module
    """

    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.game = Game(file_manager, touch, display, tarot, morse_code, encryption)

    def tearDown(self):
        """
        tearDown class
        """
        pass

    def test_multiple_choice_won(self):
        """
        test multiple_choice won functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        question_bank = data.tarot_trivia_game
        game_number = '1'
        num_questions = 2
        num_questions_to_win = 1
        # Returns
        return_1 = '1 '
        # Calls
        won_game = self.game.multiple_choice(question_bank, game_number, num_questions, num_questions_to_win)
        if won_game:
            self.game.won(won_game)
        # Asserts
        self.assertEqual(won_game, return_1)

    def test_multiple_choice_lose(self):
        """
        test multiple_choice lose functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        question_bank = data.tarot_trivia_game
        game_number = '1'
        num_questions = 2
        num_questions_to_win = 1
        # Returns
        return_1 = False
        # Calls
        won_game = self.game.multiple_choice(question_bank, game_number, num_questions, num_questions_to_win)
        if won_game:
            self.game.won(won_game)
        # Asserts
        self.assertEqual(won_game, return_1)

    def test_multiple_choice_practice(self):
        """
        test multiple_choice practice functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        question_bank = data.tarot_trivia_game
        # Returns
        return_1 = None
        # Calls
        none_1 = self.game.multiple_choice_practice(question_bank)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_morse_code_won(self):
        """
        test morse_code won functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        question_bank = data.morse_code_game
        game_number = '7'
        num_questions = 2
        num_questions_to_win = 1
        # Returns
        return_1 = '7 '
        # Calls
        won_game = self.game.morse_code_sequence(question_bank, game_number, num_questions, num_questions_to_win)
        if won_game:
            self.game.won(won_game)
        # Asserts
        self.assertEqual(won_game, return_1)

    def test_morse_code_lose(self):
        """
        test morse_code lose functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        question_bank = data.morse_code_game
        game_number = '7'
        num_questions = 2
        num_questions_to_win = 1
        # Returns
        return_1 = False
        # Calls
        won_game = self.game.morse_code_sequence(question_bank, game_number, num_questions, num_questions_to_win)
        # Asserts
        self.assertEqual(won_game, return_1)

    def test_sequence_won(self):
        """
        test seqience won functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        question_bank = data.stego_game
        game_number = '7'
        num_questions = 1
        num_questions_to_win = 1
        # Returns
        return_1 = '7 '
        # Calls
        won_game = self.game.sequence(question_bank, game_number, num_questions, num_questions_to_win)
        if won_game:
            self.game.won(won_game)
        # Asserts
        self.assertEqual(won_game, return_1)

    def test_sequence_lose(self):
        """
        test sequence lose functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        question_bank = data.stego_game
        game_number = '7'
        num_questions = 1
        num_questions_to_win = 1
        # Returns
        return_1 = False
        # Calls
        won_game = self.game.sequence(question_bank, game_number, num_questions, num_questions_to_win)
        # Asserts
        self.assertEqual(won_game, return_1)

    def test_won(self):
        """
        test won functionality
        """
        # Params
        game_won = '1'
        # Returns
        return_1 = False
        # Calls
        none_1 = self.game.won(game_won)
        # Asserts
        self.assertEqual(none_1, return_1)


if __name__ == '__main__':
    unittest.main()
