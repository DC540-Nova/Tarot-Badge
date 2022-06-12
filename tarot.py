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

import random

from config import button, display
from data import ham_radio_questions


def reading(card_bank):
    """
    Function to handle a tarot reading

    Params:
        card_bank, dict
    """
    reading = list(card_bank)  # noqa
    counter = 1
    for _ in card_bank:
        card, card_reading = random.choice(list(card_bank.items()))
        meaning = random.randint(1, 2)  # randomize card up or down position
        if counter == 1:
            display.text('Querent', timed=False)
        elif counter == 2:
            display.text('Obstacle', timed=False)
        elif counter == 3:
            display.text('Influences', timed=False)
        elif counter == 4:
            display.text('Root', timed=False)
        elif counter == 5:
            display.text('Past', timed=False)
        elif counter == 6:
            display.text('Future', timed=False)
        elif counter == 7:
            display.text('Attitude', timed=False)
        elif counter == 8:
            display.text('Environment', timed=False)
        elif counter == 9:
            display.text('Hopes & Fears', timed=False)
        elif counter == 10:
            display.text('Outcome', timed=False)
        button.press()
        if meaning == 1:
            display.image('sd/' + card_reading[2], timed=False)
        elif meaning == 2:
            display.image('sd/' + card_reading[2], up=False, timed=False)
        if meaning == 1:
            display.text(card_reading[0], timed=False)
        elif meaning == 2:
            display.text(card_reading[1], timed=False)
        button.press()
        counter += 1
        del card_bank[card]
        if counter > 10:
            display.POWER_DISPLAY.value(0)
            display.clear()
            break
