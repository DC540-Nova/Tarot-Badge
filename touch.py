# # MIT License
# #
# # Designer: Bob German
# # Designer: Betsy Lawrie
# # Developer: Kevin Thomas
# # Developer: Corinne "Rinn" Neidig
# #
# # Copyright (c) 2022 DC540 Defcon Group
# #
# # Permission is hereby granted, free of charge, to any person obtaining a copy
# # of this software and associated documentation files (the "Software"), to deal
# # in the Software without restriction, including without limitation the rights
# # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the Software is
# # furnished to do so, subject to the following conditions:
# #
# # The above copyright notice and this permission notice shall be included in all
# # copies or substantial portions of the Software.
# #
# # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# # SOFTWARE.
#
# # pyright: reportMissingImports=false
# # pyright: reportUndefinedVariable=false
#
from machine import Pin
from utime import sleep


class Touch:
    """
    Base class to handle capacitive touch button presses
    """

    def __init__(self, button_up, button_down, button_left, button_right, button_submit, button_extra, display,
                 wait=0.05, sensitivity=6):
        """
        Params:
            button_up: int
            button_down: int
            button_left: int
            button_right: int
            button_submit: int
            button_extra: int
            display: object
            wait: float, optional
            sensitivity: int, optional
        """
        self.button_left = button_left
        self.button_right = button_right
        self.button_up = button_up
        self.button_down = button_down
        self.button_submit = button_submit
        self.button_extra = button_extra
        self.display = display
        self.wait = wait
        self.sensitivity = sensitivity
        self.start_time = 0
        self.button_total_value = 0

    def press(self, gpio):
        """
        Method to handle a capacitive touch button press

        Params:
            gpio: int

        Returns:
            bool
        """
        self.start_time = 0
        self.button_total_value = 0
        button = Pin(gpio, Pin.OUT)
        button.value(1)
        button = Pin(gpio, Pin.IN)
        while self.start_time < self.sensitivity:
            button_value = button.value()
            self.button_total_value += button_value
            self.start_time += 1
        if self.button_total_value == self.sensitivity:
            print(self.button_total_value)
            sleep(self.wait)
            return True
        else:
            print(self.button_total_value)
            sleep(self.wait)
            return False

    def yes_no(self):
        """
        Method to handle a yes/no response from a touch button press

        Returns:
            str
        """
        while True:
            if self.press(self.button_left):
                return 'yes'
            elif self.press(self.button_right):
                return 'no'

    def multiple_choice(self):
        """
        Method to handle a single multiple choice response from a touch button press

        Returns:
            str
        """
        while True:
            if self.press(self.button_left):
                return 0
            elif self.press(self.button_right):
                return 1
            elif self.press(self.button_up):
                return 2
            elif self.press(self.button_down):
                return 3
            elif self.press(self.button_submit):
                return 4
            elif self.press(self.button_extra):
                return 5

    def morse_code(self, max_chars=20):
        """
        Method to handle morse code touch button presses

        Params:
            max_chars: int, optional

        Returns:
            str
        """
        sentence = ''
        while True:
            if len(sentence) >= max_chars:
                sentence = ''
            if self.press(self.button_left):
                sentence += '.'
                self.display.text(sentence, timed=False)
            elif self.press(self.button_right):
                sentence += '-'
                self.display.text(sentence, timed=False)
            elif self.press(self.button_up):
                sentence += ' '
                self.display.text(sentence, timed=False)
            elif self.press(self.button_down):
                pass
            elif self.press(self.button_submit):
                pass
            elif self.press(self.button_extra):
                if sentence:
                    return sentence

    def numeric_sequence(self, max_nums=6):
        """
        Method to handle the construction of four numeric numbers as a result of a series of button presses

        Params:
            max_nums: int, optional

        Returns:
            int
        """
        numeric_sequence = ''
        while True:
            if self.press(self.button_left):
                numeric_sequence += '1'
                self.display.text(numeric_sequence, timed=False)
            elif self.press(self.button_right):
                numeric_sequence += '2'
                self.display.text(numeric_sequence, timed=False)
            elif self.press(self.button_up):
                numeric_sequence += '3'
                self.display.text(numeric_sequence, timed=False)
            elif self.press(self.button_down):
                numeric_sequence += '4'
                self.display.text(numeric_sequence, timed=False)
            elif self.press(self.button_submit):
                pass
            elif self.press(self.button_extra):
                if numeric_sequence:
                    return numeric_sequence
            if len(numeric_sequence) > max_nums:
                numeric_sequence = ''
