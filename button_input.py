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

from config import *


class ButtonInput:
    """
    Class to handle building strings with buttons
    """

    def __init__(self):
        self.multiple_choice_letters = [
            'A',
            'B',
            'C',
            'D'
        ]
        self.y_n_letters = [
            'Y',
            'N'
        ]
        self.word = ''
        self.position = 0
        self.char_position = 0
        self.multiple_choice_letters_length = len(self.multiple_choice_letters) - 1
        self.y_n_letters_length = len(self.y_n_letters) - 1
        self.press_time = 0.50

    def get_response(self, input_type='numbers'):
        """
        Method to handle a button press for get_response logic

        Params:
            input_type: str, optional

        Returns:
            int, char
        """
        if input_type == 'multiple_choice_letters':
            self.word = ''
            self.position = 0
            self.char_position = 0
            display.text(self.multiple_choice_letters[self.position])
            while True:
                if not BUTTON_UP.value():
                    if self.position >= self.multiple_choice_letters_length:
                        sleep(self.press_time)
                    else:
                        self.position += 1
                        display.text(self.word)
                        display.text(self.multiple_choice_letters[self.position], x=self.char_position,
                                     start_clear=False)
                        sleep(self.press_time)
                elif not BUTTON_DOWN.value():
                    if self.position <= 0:
                        sleep(self.press_time)
                    else:
                        self.position -= 1
                        display.text(self.word)
                        display.text(self.multiple_choice_letters[self.position], x=self.char_position,
                                     start_clear=False)
                        sleep(self.press_time)
                elif not BUTTON_RIGHT.value():
                    self.word += self.multiple_choice_letters[self.position]
                    display.text(self.word + '_')
                    self.char_position += 8
                    sleep(self.press_time)
                elif not BUTTON_LEFT.value():
                    if len(self.word) == 1:
                        self.word = self.word[0:-1]
                        display.text(self.word)
                        display.text(self.multiple_choice_letters[self.position])
                        self.char_position -= 8
                    elif len(self.word) > 1:
                        self.word = self.word[0:-1]
                        display.text(self.word)
                        self.char_position -= 8
                    sleep(self.press_time)
                elif not BUTTON_SUBMIT.value():
                    if self.word:
                        self.word = str(self.word)
                        return self.word
        elif input_type == 'y_n_letters':
            self.word = ''
            self.position = 0
            self.char_position = 0
            display.text(self.y_n_letters[self.position])
            while True:
                if not BUTTON_UP.value():
                    if self.position >= self.y_n_letters_length:
                        sleep(self.press_time)
                    else:
                        self.position += 1
                        display.text(self.word)
                        display.text(self.y_n_letters[self.position], x=self.char_position, start_clear=False)
                        sleep(self.press_time)
                elif not BUTTON_DOWN.value():
                    if self.position <= 0:
                        sleep(self.press_time)
                    else:
                        self.position -= 1
                        display.text(self.word)
                        display.text(self.y_n_letters[self.position], x=self.char_position, start_clear=False)
                        sleep(self.press_time)
                elif not BUTTON_RIGHT.value():
                    self.word += self.y_n_letters[self.position]
                    display.text(self.word + '_')
                    self.char_position += 8
                    sleep(self.press_time)
                elif not BUTTON_LEFT.value():
                    if len(self.word) == 1:
                        self.word = self.word[0:-1]
                        display.text(self.word)
                        display.text(self.y_n_letters[self.position])
                        self.char_position -= 8
                    elif len(self.word) > 1:
                        self.word = self.word[0:-1]
                        display.text(self.word)
                        self.char_position -= 8
                    sleep(self.press_time)
                elif not BUTTON_SUBMIT.value():
                    self.word = str(self.word)
                    return self.word
