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

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

from utime import sleep


class Button:
    """
    Base class to handle button presses
    """

    def __init__(self, button_up, button_down, button_left, button_right, button_submit, button_extra, display,
                 press_time=0.10):
        """
        Params:
            button_up: object
            button_down: object
            button_left: object
            button_right: object
            button_submit: object
            button_extra: object
            display: object
            press_time: float, optional
        """
        self.button_up = button_up
        self.button_down = button_down
        self.button_left = button_left
        self.button_right = button_right
        self.button_submit = button_submit
        self.button_extra = button_extra
        self.display = display
        self.press_time = press_time

    def numeric_sequence(self, max_nums=6):
        """
        Method to handle the construction of four numeric numbers as a result of a series of button presses

        Params:
            max_nums: int, optional

        Returns:
            int
        """
        word = ''
        while True:
            if len(word) >= max_nums:
                word = ''
            if not self.button_left.value():
                word += '1'
                self.display.text(word, timed=False)
                sleep(self.press_time)
            elif not self.button_right.value():
                word += '2'
                self.display.text(word, timed=False)
                sleep(self.press_time)
            elif not self.button_up.value():
                word += '3'
                self.display.text(word, timed=False)
                sleep(self.press_time)
            elif not self.button_down.value():
                word += '4'
                self.display.text(word, timed=False)
                sleep(self.press_time)
            elif not self.button_submit.value():
                if word:
                    word = int(word)
                    return word

    def multiple_choice(self):
        """
        Method to handle a single multiple choice response from a button press

        Returns:
            str
        """
        while True:
            if not self.button_left.value():
                return 1
            elif not self.button_right.value():
                return 2
            elif not self.button_up.value():
                return 3
            elif not self. button_down.value():
                return 4
            elif not self. button_submit.value():
                return 5
            elif not self. button_extra.value():
                return 6

    def yes_no(self):
        """
        Method to handle a yes/no response from a button press

        Returns:
            str
        """
        while True:
            if not self.button_left.value():
                return 'yes'
            elif not self.button_right.value():
                return 'no'

    def morse_code(self, max_chars=8):
        """
        Method to handle morse code button presses

        Params:
            max_chars: int, optional

        Returns:
            str
        """
        word = ''
        while True:
            if len(word) >= max_chars:
                word = ''
            if not self.button_left.value():
                word += '.'
                self.display.text(word, timed=False)
                sleep(self.press_time)
            elif not self.button_right.value():
                word += '-'
                self.display.text(word, timed=False)
                sleep(self.press_time)
            elif not self.button_up.value():
                word += ' '
                self.display.text(word, timed=False)
                sleep(self.press_time)
            elif not self.button_submit.value():
                if word:
                    return word

    def press(self):
        """
        Method to handle a button press
        """
        while True:
            if not self.button_left.value():
                return 1
            elif not self.button_right.value():
                return 2
            elif not self.button_up.value():
                return 3
            elif not self. button_down.value():
                return 4
            elif not self. button_submit.value():
                return 5
            elif not self. button_extra.value():
                return 6
