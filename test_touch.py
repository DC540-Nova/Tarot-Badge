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
# unittest.main('test_touch')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import utime
import unittest

from config import BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display
from touch import Touch


class TestMicrocontroller(unittest.TestCase):
    """
    Test class to test microcontroller module
    """
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.touch = Touch(BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display)

    @staticmethod
    def tearDown():
        """
        tearDown class
        """
        # Sleep between tests
        utime.sleep(1)

    def test_press_button_left(self):
        """
        test press button_left functionality

        Interactive Response:  [PRESS BUTTON_LEFT BUTTON]
        """
        # Params
        true_1 = False
        # Returns
        return_1 = True
        # Calls
        while not true_1:
            true_1 = self.touch.press(self.touch.button_left)
        # Asserts
        self.assertEqual(true_1, return_1)

    def test_press_button_right(self):
        """
        test press button_right functionality

        Interactive Response:  [PRESS BUTTON_RIGHT BUTTON]
        """
        # Params
        true_1 = False
        # Returns
        return_1 = True
        # Calls
        while not true_1:
            true_1 = self.touch.press(self.touch.button_right)
        # Asserts
        self.assertEqual(true_1, return_1)

    def test_press_button_up(self):
        """
        test press button_up functionality

        Interactive Response:  [PRESS BUTTON_UP BUTTON]
        """
        # Params
        true_1 = False
        # Returns
        return_1 = True
        # Calls
        while not true_1:
            true_1 = self.touch.press(self.touch.button_up)
        # Asserts
        self.assertEqual(true_1, return_1)

    def test_press_button_down(self):
        """
        test press button_down functionality

        Interactive Response:  [PRESS BUTTON_DOWN BUTTON]
        """
        # Params
        true_1 = False
        # Returns
        return_1 = True
        # Calls
        while not true_1:
            true_1 = self.touch.press(self.touch.button_down)
        # Asserts
        self.assertEqual(true_1, return_1)

    def test_press_button_submit(self):
        """
        test press button_submit functionality

        Interactive Response:  [PRESS BUTTON_SUBMIT BUTTON]
        """
        # Params
        true_1 = False
        # Returns
        return_1 = True
        # Calls
        while not true_1:
            true_1 = self.touch.press(self.touch.button_submit)
        # Asserts
        self.assertEqual(true_1, return_1)

    def test_press_button_extra(self):
        """
        test press button_extra functionality

        Interactive Response:  [PRESS BUTTON_EXTRA BUTTON]
        """
        # Params
        true_1 = False
        # Returns
        return_1 = True
        # Calls
        while not true_1:
            true_1 = self.touch.press(self.touch.button_extra)
        # Asserts
        self.assertEqual(true_1, return_1)

    def test_yes_no_yes(self):
        """
        test yes_no yes functionality

        Interactive Response:  [PRESS BUTTON_LEFT BUTTON]
        """
        # Params
        yes = None
        # Returns
        return_1 = 'yes'
        # Calls
        while not yes:
            yes = self.touch.yes_no()
        # Asserts
        self.assertEqual(yes, return_1)

    def test_yes_no_no(self):
        """
        test yes_no no functionality

        Interactive Response:  [PRESS BUTTON_RIGHT BUTTON]
        """
        # Params
        no = None
        # Returns
        return_1 = 'no'
        # Calls
        while not no:
            no = self.touch.yes_no()
        # Asserts
        self.assertEqual(no, return_1)

    # NOTE: `test_multiple_choice_button_left` returns 0 and can only be tested manually

    def test_multiple_choice_button_right(self):
        """
        test multiple_choice button right functionality

        Interactive Response:  [PRESS BUTTON_RIGHT BUTTON]
        """
        # Params
        number = None
        # Returns
        return_1 = 1
        # Calls
        while not number:
            number = self.touch.multiple_choice()
        # Asserts
        self.assertEqual(number, return_1)

    def test_multiple_choice_button_up(self):
        """
        test multiple_choice button up functionality

        Interactive Response:  [PRESS BUTTON_UP BUTTON]
        """
        # Params
        number = None
        # Returns
        return_1 = 2
        # Calls
        while not number:
            number = self.touch.multiple_choice()
        # Asserts
        self.assertEqual(number, return_1)

    def test_multiple_choice_button_down(self):
        """
        test multiple_choice button down functionality

        Interactive Response:  [PRESS BUTTON_DOWN BUTTON]
        """
        # Params
        number = None
        # Returns
        return_1 = 3
        # Calls
        while not number:
            number = self.touch.multiple_choice()
        # Asserts
        self.assertEqual(number, return_1)

    def test_multiple_choice_button_submit(self):
        """
        test multiple_choice button submit functionality

        Interactive Response:  [PRESS BUTTON_SUBMIT BUTTON]
        """
        # Params
        number = None
        # Returns
        return_1 = 4
        # Calls
        while not number:
            number = self.touch.multiple_choice()
        # Asserts
        self.assertEqual(number, return_1)

    def test_multiple_choice_button_extra(self):
        """
        test multiple_choice button extra functionality

        Interactive Response:  [PRESS BUTTON_EXTRA BUTTON]
        """
        # Params
        number = None
        # Returns
        return_1 = 5
        # Calls
        while not number:
            number = self.touch.multiple_choice()
        # Asserts
        self.assertEqual(number, return_1)

    def test_morse_code(self):
        """
        test morse_code functionality

        Interactive Response:  [PRESS BUTTON_LEFT, BUTTON_UP, BUTTON_RIGHT BUTTON]
        """
        # Params
        sentence = None
        # Returns
        return_1 = '. -'
        # Calls
        while not sentence:
            sentence = self.touch.morse_code()
        # Asserts
        self.assertEqual(sentence, return_1)

    def test_numeric_sequence(self):
        """
        test numeric_sequence functionality

        Interactive Response:  [PRESS BUTTON_LEFT, BUTTON_RIGHT, BUTTON_UP, BUTTON_DOWN BUTTON]
        """
        # Params
        numeric_sequence = None
        # Returns
        return_1 = '1234'
        # Calls
        while not numeric_sequence:
            numeric_sequence = self.touch.morse_code()
        # Asserts
        self.assertEqual(numeric_sequence, return_1)
