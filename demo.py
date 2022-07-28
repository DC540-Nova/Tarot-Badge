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

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import _thread
from utime import sleep
import random
# import gc


class Demo:
    """
    Base class to handle the demo
    """

    def __init__(self, touch, display, neo_pixel):
        """
        Params:
            touch: object
            display: object
            neo_pixel: object
        """
        self.touch = touch
        self.display = display
        self.neo_pixel = neo_pixel
        self.thread = False

    def __bg_task(self):
        """
        Private method to handle multi-threadded functionality
        """
        self.thread = True
        # gc.collect()
        hex1 = [32, 31, 30, 27, 28, 29, 32]
        paths = [28, 30, 29, 26, 22, 21, 23, 24, 19, 14, 13, 16, 17, 12, 11, 10, 8, 6, 3, 5, 2, 1]
        while True:
            for _ in range(25):
                for my_LED in hex1:
                    self.neo_pixel.on(paths[my_LED - 11], self.neo_pixel.COLORS[random.randint(1, 7)])
                    if not self.thread:
                        _thread.exit()
            for _ in range (5):
                for _ in paths:
                    self.neo_pixel.flicker()
                    if not self.thread:
                        _thread.exit()
            for _ in range(5):
                for my_LED in paths:
                    self.neo_pixel.breathing_led_on(my_LED)
                    if not self.thread:
                        _thread.exit()

    def play(self):
        """
        Method to handle demo play
        """
        _thread.start_new_thread(self.__bg_task, ())  # noqa
        self.display.handle_threading_setup()
        while True:
            touched = self.touch.press(self.touch.button_left)
            if touched:
                self.thread = False
                self.neo_pixel.clear(hard_clear=True)
                break
            try:
                self.display.image('sd/Rider-Waite/00-TheFool.raw', multithreading=True)
            except OSError:
                self.display.text('sd card is damaged')
            self.display.handle_threading_teardown()
            self.display.handle_threading_setup()
            #_thread.start_new_thread(self.__bg_task, ())  # noqa
            touched = self.touch.press(self.touch.button_left)
            if touched:
                self.thread = False
                self.neo_pixel.clear(hard_clear=True)
                break
            try:
                self.display.image('sd/Rider-Waite/01-TheMagician.raw', multithreading=True)
            except OSError:
                self.display.text('sd card is damaged')
            self.display.handle_threading_teardown()
            self.display.handle_threading_setup()
            #_thread.start_new_thread(self.__bg_task, ())  # noqa
            touched = self.touch.press(self.touch.button_left)
            if touched:
                self.thread = False
                self.neo_pixel.clear(hard_clear=True)
                break
            try:
                self.display.image('sd/Rider-Waite/02-TheHighPriestess.raw', multithreading=True)
            except OSError:
                self.display.text('sd card is damaged')
            self.display.handle_threading_teardown()
            self.display.handle_threading_setup()
            #_thread.start_new_thread(self.__bg_task, ())  # noqa


