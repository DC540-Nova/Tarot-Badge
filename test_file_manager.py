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
# unittest.main('test_file_manager')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest
import uos

from main import button_up, button_down, button_left, button_right, button_submit, button_extra, display, neo_pixel
from touch import Touch
from file_manager import FileManager

touch = Touch(button_up, button_down, button_left, button_right, button_submit, button_extra, display)


class TestFileManager(unittest.TestCase):
    """
    Test class to test file_manager module
    """
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.file_manager = FileManager(touch, display, neo_pixel)
        # Clear Files
        self.file_manager.clear_ids_file()
        self.file_manager.clear_games_won_file()

    @staticmethod
    def tearDown():
        """
        tearDown class
        """
        # Clear LEDs
        neo_pixel.clear(hard_clear=True)

    def test_write_ids_file(self):
        """
        test write_ids_file functionality
        """
        # Params
        ids = 'e66038b713902e33'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.file_manager.write_ids_file(ids)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_read_ids_file(self):
        """
        test read_ids_file functionality
        """
        # Params
        ids = 'e66038b713902e33'
        # Returns
        return_1 = 'e66038b713902e33'
        # Calls
        self.file_manager.write_ids_file(ids)
        ids = self.file_manager.read_ids_file()
        # Asserts
        self.assertEqual(ids, return_1)

    def test_write_games_won_file(self):
        """
        test write_games_won functionality
        """
        # Params
        games_won = '66 23 89 40 98 11 15 37 71 53 94 69'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.file_manager.write_games_won_file(games_won)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_read_games_won_file(self):
        """
        test read_games_won_file functionality
        """
        # Params
        games_won = '66 23 89 40 98 11 15 37 71 53 94 69'
        # Returns
        return_1 = '66 23 89 40 98 11 15 37 71 53 94 69'
        # Calls
        self.file_manager.write_games_won_file(games_won)
        games_won = self.file_manager.read_games_won_file()
        # Asserts
        self.assertEqual(games_won, return_1)

    def test_write_tarot_deck_folder(self):
        """
        test write_tarot_deck_folder functionality
        """
        # Params
        tarot_deck_folder = 'Rider-Waite'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.file_manager.write_tarot_deck_folder(tarot_deck_folder)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_read_tarot_deck_folder(self):
        """
        test read_tarot_deck_folder functionality
        """
        # Returns
        return_1 = 'Rider-Waite'
        # Calls
        none_1 = self.file_manager.read_tarot_deck_folder()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_clear_ids_file(self):
        """
        test clear_ids_file functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.file_manager.clear_ids_file()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_clear_games_won_file(self):
        """
        test clear_games_won_file functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.file_manager.clear_games_won_file()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_update_games_won(self):
        """
        test update_games_won functionality
        """
        # Params
        games_won = '66 23 89 40 98 11 15 37 71 53 94 69'
        # Returns
        return_1 = None
        # Calls
        self.file_manager.write_games_won_file(games_won)
        none_1 = self.file_manager.update_games_won()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_clear_ids(self):
        """
        test clear ids file functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.file_manager.clear_ids_file()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_clear_games_won(self):
        """
        test clear games_won file functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.file_manager.clear_games_won_file()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_reset(self):
        """
        test reset badge functionality

        Interactive Response:  [RANDOM MANUAL VALIDATION]
        """
        # Params
        file = 'games_won'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.file_manager.reset(file)
        # Asserts
        self.assertEqual(none_1, return_1)


if __name__ == '__main__':
    unittest.main()
