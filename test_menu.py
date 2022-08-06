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
# unittest.main('test_menu')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from config import BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display, neo_pixel, \
    nrf
from microcontroller import Microcontroller
from encryption import Encryption
from touch import Touch
from file_manager import FileManager
from demo import Demo
from tarot import Tarot
from bad_advice import BadAdvice
from game import Game
from morse_code import MorseCode
from pair import Pair
from menu import Menu
import data


class TestMenu(unittest.TestCase):
    """
    Test class to test menu module
    """
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.menu = Menu(file_manager, touch, display, neo_pixel, game, tarot, bad_advice, pair, demo, data)

    def tearDown(self):
        """
        tearDown class
        """
        pass

    def test_get_unique_id(self):
        """
        test get_unique_id functionality
        """
        # Returns
        return_1 = 'e66038b713902e33'
        # Calls
        my_id_hex = self.microcontroller.get_unique_id()
        # Asserts
        self.assertEqual(my_id_hex, return_1)

    # NOTE: `system` is an infinite menu loop and can only be tested manually
