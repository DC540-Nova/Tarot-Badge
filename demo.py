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
from utime import sleep
from urandom import randrange, choice
import machine
from neopixel import NeoPixel


class Demo:
    """
    Base class to handle the demo
    """

    def __init__(self, touch, display, neo_pixel, data):
        """
        Params:
            touch: object
            display: object
            neo_pixel: object
            data: object
        """
        self.neopixel = NeoPixel(machine.Pin(5), 24)
        self.touch = touch
        self.display = display
        self.neo_pixel = neo_pixel
        self.data = data
        self.thread = False
        # color change interval
        self.cint = 10
        self.cmin = 0
        self.cmax = 128
        self.max_pos = 12
        self.stime = 0.05
        self.owheelpos = 1
        self.iwheelpos = 1
        # outer ring color settings
        self.ocr = self.cmin
        self.ocg = self.cmin
        self.ocb = self.cmax
        # inner ring color settings
        self.icr = self.cmax
        self.icg = self.cmin
        self.icb = self.cmin
        # wheel definitions for neopixel
        self.owheel = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.iwheel = [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]

    def __reset(self):
        """
        Private method to reset original neo_pixel object and clear pixels
        """
        LED_PIN = 5
        LED_COUNT = 24
        from neo_pixel import NeoPixel  # noqa
        self.neo_pixel = NeoPixel(machine.Pin, LED_PIN, LED_COUNT)
        self.neo_pixel.clear(hard_clear=True)

    def __new_color(self, my_color):
        """
        Private method to color changes, called for each color

        Params:
            my_color: int
        """
        my_new_color = my_color + randrange(-self.cint, self.cint)
        if my_new_color > self.cmax:
            my_new_color = my_new_color - (self.cmax - self.cmin)
        if my_new_color < self.cmin:
            my_new_color = my_new_color + (self.cmax - self.cmin)
        return my_new_color

    def __neopixel_animation(self):
        """
        Private method to handle the neopixel animation on the second core
        """
        while True:
            try:
                try:
                    self.thread = True
                    self.neopixel[self.owheel[self.owheelpos - 1] - 1] = (self.ocr, self.ocg, self.ocb)
                    self.neopixel[self.iwheel[self.iwheelpos - 1] - 1] = (self.icr, self.icg, self.icb)
                    self.neopixel.write()
                    if not self.thread:
                        self.__reset()
                        _thread.exit()
                    while True:
                        self.neopixel[self.owheel[self.owheelpos - 1] - 1] = (self.ocr, self.ocg, self.ocb)
                        self.neopixel[self.iwheel[self.iwheelpos - 1] - 1] = (self.icr, self.icg, self.icb)
                        self.neopixel.write()
                        if not self.thread:
                            self.__reset()
                            _thread.exit()
                        x = int(randrange(-10, 10))
                        y = int(randrange(-10, 10))
                        new_outer = 0
                        stime = randrange(5, 6) / 100
                        # stime = randrange(5, 6) / 1000
                        if not self.thread:
                            self.__reset()
                            _thread.exit()
                        for count in range(max(abs(x), abs(y))):
                            if x:
                                x_inc = int(x / abs(x))
                                new_outer = self.owheelpos + x_inc
                                x = x - x_inc
                            if new_outer > self.max_pos:
                                new_outer = 1
                            if new_outer < 1:
                                new_outer = self.max_pos
                            if not self.thread:
                                self.__reset()
                                _thread.exit()
                            if y:
                                y_inc = int(y / abs(y))
                                new_inner = self.iwheelpos + y_inc
                                y = y - y_inc
                                if new_inner > self.max_pos:
                                    new_inner = 1
                                if new_inner < 1:
                                    new_inner = self.max_pos
                                sleep(stime)
                                self.ocr = self.__new_color(self.ocr)
                                self.ocg = self.__new_color(self.ocg)
                                self.ocb = self.__new_color(self.ocb)
                                self.icr = self.__new_color(self.ocr)
                                self.icg = self.__new_color(self.ocg)
                                self.icb = self.__new_color(self.ocb)
                                oold = self.owheel[self.owheelpos - 1] - 1
                                iold = self.iwheel[self.iwheelpos - 1] - 1
                                self.owheelpos = new_outer
                                self.iwheelpos = new_inner
                                onum = self.owheel[self.owheelpos - 1] - 1
                                inum = self.iwheel[self.iwheelpos - 1] - 1
                                self.neopixel[onum] = (self.ocr, self.ocg, self.ocg)
                                self.neopixel[inum] = (self.icr, self.icg, self.icb)
                                self.neopixel[oold] = (0, 0, 0)
                                self.neopixel[iold] = (0, 0, 0)
                                self.neopixel.write()
                            if not self.thread:
                                self.__reset()
                                _thread.exit()
                except KeyboardInterrupt:
                    pass
            except KeyboardInterrupt:
                pass

    def play(self):
        """
        Method to handle demo play
        """
        _thread.start_new_thread(self.__neopixel_animation, ())
        self.display.handle_threading_setup()
        running = True
        while running:
            for _ in self.data.cards:
                card, card_reading = choice(list(self.data.cards.items()))
                try:
                    card = 'sd/' + 'Rider-Waite' + '/' + card_reading[2]
                    self.display.image(card)
                    touched = self.touch.press(self.touch.button_left)
                    if touched:
                        self.thread = False
                        running = False
                        break
                except OSError:
                    self.display.text('sd card is damaged')
                    break
