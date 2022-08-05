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
# unittest.main('test_bad_advice')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from config import BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display, neo_pixel
from touch import Touch
from bad_advice import BadAdvice
import data

touch = Touch(BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display)


class TestBadAdvice(unittest.TestCase):
    """
    Test class to test bad_advice module
    """
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.bad_advice = BadAdvice(touch, display, neo_pixel)

    @staticmethod
    def tearDown():
        """
        tearDown class
        """
        # Clear LED's
        neo_pixel.clear(hard_clear=True)

    def test_bad_advice_scroll(self):
        """
        test bad advice scroll functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.bad_advice.scroll()
        # Asserts
        self.assertEqual(none_1, return_1)
