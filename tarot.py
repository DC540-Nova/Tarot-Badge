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

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import _thread
import urandom


class Tarot:
    """
    Base class to handle tarot card reading/s
    """

    def __init__(self, touch, display, neo_pixel, card_bank):
        """
        Params:
            touch: object
            display: object
            neo_pixel: object
            card_bank: dict
        """
        self.touch = touch
        self.display = display
        self.neo_pixel = neo_pixel
        self.card_bank = card_bank
        self.thread = False

    def __neopixel_animation(self):
        """
        Private method to handle the neopixel animation on the second core
        """
        self.thread = True
        while True:
            self.neo_pixel.breathing_led_on()
            if not self.thread:
                self.neo_pixel.clear(hard_clear=True)
                _thread.exit()

    def reading(self, deck):
        """
        Function to handle a tarot reading

        Params:
            deck: int
        """
        _thread.start_new_thread(self.__neopixel_animation, ())
        self.display.handle_threading_setup()
        temp_card_bank = self.card_bank
        counter = 1
        for _ in temp_card_bank:
            card, card_reading = urandom.choice(list(temp_card_bank.items()))
            meaning = urandom.randint(1, 2)  # randomize card up or down position
            if counter == 1:
                self.display.text('Querent')
            elif counter == 2:
                self.display.text('Obstacle')
            elif counter == 3:
                self.display.text('Influences')
            elif counter == 4:
                self.display.text('Root')
            elif counter == 5:
                self.display.text('Past')
            elif counter == 6:
                self.display.text('Future')
            elif counter == 7:
                self.display.text('Attitude')
            elif counter == 8:
                self.display.text('Environment')
            elif counter == 9:
                self.display.text('Hopes & Fears')
            elif counter == 10:
                self.display.text('Outcome')
            if meaning == 1:
                try:
                    card = 'sd/' + deck + '/' + card_reading[2]
                    self.display.image(card, timed=False)
                    while True:
                        if self.touch.press(self.touch.button_left):
                            break
                except OSError:
                    self.display.text('sd card is damaged')
                    break
            if meaning == 2:
                try:
                    card = 'sd/' + deck + '/' + card_reading[2]
                    self.display.image(card, up=False, timed=False)
                    while True:
                        if self.touch.press(self.touch.button_left):
                            break
                except OSError:
                    self.display.text('sd card is damaged')
                    break
            if meaning == 1:
                self.display.text(card_reading[0], timed=False)
                while True:
                    if self.touch.press(self.touch.button_left):
                        break
            if meaning == 2:
                self.display.text(card_reading[1], timed=False)
                while True:
                    if self.touch.press(self.touch.button_left):
                        break
            counter += 1
            try:
                del temp_card_bank[card]
            except KeyError:
                pass
            if counter > 10:
                self.display.POWER_DISPLAY.value(0)
                self.display.clear()
                self.thread = False
                break

    def scroll(self, deck):
        """
        Function to handle a tarot scroll

        Params:
            deck: object
        """
        _thread.start_new_thread(self.__neopixel_animation, ())
        self.display.handle_threading_setup()
        running = True
        while running:
            card_bank = self.card_bank
            for _ in card_bank:
                touched = self.touch.press(self.touch.button_left)
                if touched:
                    self.thread = False
                    running = False
                    break
                card, card_reading = urandom.choice(list(self.card_bank.items()))
                try:
                    card = 'sd/' + deck + '/' + card_reading[2]
                    self.display.image(card)
                except OSError:
                    self.display.text('sd card is damaged')
                    break
