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
# y
# SOFTWARE.

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import random


class Tarot:
    """
    Base class to handle tarot card reading/s
    """

    def __init__(self, button, display, card_bank):
        """
        Params:
            button: object
            display: object
            card_bank: dict
        """
        self.button = button
        self.display = display
        self.card_bank = card_bank

    def reading(self):
        """
        Function to handle a tarot reading

        Params:
            card_bank, dict
        """
        # reading = list(self.card_bank)  # noqa
        counter = 1
        for _ in self.card_bank:
            card, card_reading = random.choice(list(self.card_bank.items()))
            meaning = random.randint(1, 2)  # randomize card up or down position
            if counter == 1:
                self.display.text('Querent', timed=False)
            elif counter == 2:
                self.display.text('Obstacle', timed=False)
            elif counter == 3:
                self.display.text('Influences', timed=False)
            elif counter == 4:
                self.display.text('Root', timed=False)
            elif counter == 5:
                self.display.text('Past', timed=False)
            elif counter == 6:
                self.display.text('Future', timed=False)
            elif counter == 7:
                self.display.text('Attitude', timed=False)
            elif counter == 8:
                self.display.text('Environment', timed=False)
            elif counter == 9:
                self.display.text('Hopes & Fears', timed=False)
            elif counter == 10:
                self.display.text('Outcome', timed=False)
            _ = self.button.press()
            if meaning == 1:
                self.display.image('sd/' + card_reading[2], timed=False)
            if meaning == 2:
                self.display.image('sd/' + card_reading[2], up=False, timed=False)
            _ = self.button.press()
            if meaning == 1:
                self.display.text(card_reading[0], timed=False)
            if meaning == 2:
                self.display.text(card_reading[1], timed=False)
            _ = self.button.press()
            counter += 1
            del self.card_bank[card]
            if counter > 10:
                self.display.POWER_DISPLAY.value(0)
                self.display.clear()
                break
