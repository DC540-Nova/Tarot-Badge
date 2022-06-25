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

from config import BUTTON_UP, BUTTON_DOWN, BUTTON_LEFT, BUTTON_RIGHT, BUTTON_SUBMIT, BUTTON_EXTRA, display


def numeric_sequence(press_time=0.10, max_nums=6):
    """
    Function to handle the construction of four numeric numbers as a result of a series of button presses

    Params:
        press_time: float, optional
        max_nums: int, optional

    Returns:
        int
    """
    word = ''
    while True:
        if len(word) >= max_nums:
            word = ''
        if not BUTTON_UP.value():
            word += '1'
            display.text(word, timed=False)
            sleep(press_time)
        elif not BUTTON_DOWN.value():
            word += '2'
            display.text(word, timed=False)
            sleep(press_time)
        elif not BUTTON_LEFT.value():
            word += '3'
            display.text(word, timed=False)
            sleep(press_time)
        elif not BUTTON_RIGHT.value():
            word += '4'
            display.text(word, timed=False)
            sleep(press_time)
        elif not BUTTON_SUBMIT.value():
            if word:
                word = int(word)
                return word


def multiple_choice():
    """
    Function to handle a single multiple choice response from a button press

    Returns:
        str
    """
    while True:
        if not BUTTON_UP.value():
            return 0
        elif not BUTTON_DOWN.value():
            return 1
        elif not BUTTON_LEFT.value():
            return 2
        elif not BUTTON_RIGHT.value():
            return 3


def yes_no():
    """
    Function to handle a yes/no response from a button press

    Returns:
        str
    """
    while True:
        if not BUTTON_UP.value():
            return 'yes'
        elif not BUTTON_DOWN.value():
            return 'no'


def morse_code(press_time=0.10, max_chars=8):
    """
    Function to handle morse code button presses

    Params:
        press_time: float, optional
        max_chars: int, optional

    Returns:
        str
    """
    word = ''
    while True:
        if len(word) >= max_chars:
            word = ''
        if not BUTTON_UP.value():
            word += '.'
            display.text(word, timed=False)
            sleep(press_time)
        elif not BUTTON_DOWN.value():
            word += '-'
            display.text(word, timed=False)
            sleep(press_time)
        elif not BUTTON_DOWN.value():
            word += ' '
            display.text(word, timed=False)
            sleep(press_time)
        elif not BUTTON_SUBMIT.value():
            if word:
                return word


def press():
    """
    Function to handle a button press
    """
    while True:
        if not BUTTON_UP.value():
            return
        elif not BUTTON_DOWN.value():
            return
        elif not BUTTON_LEFT.value():
            return
        elif not BUTTON_RIGHT.value():
            return
        elif not BUTTON_SUBMIT.value():
            return
        elif not BUTTON_EXTRA.value():
            return
