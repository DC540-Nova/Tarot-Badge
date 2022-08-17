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

import random


class BadAdvice:
    """
    Base class to handle the bad advice demo
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

    def scroll(self):
        """
        Method to handle bad advice demo play
        """
        color = random.choice(self.neo_pixel.COLORS)
        self.neo_pixel.on(0, color=color, all_on=True)
        card = 'sd/bad_advice/ba1.raw'
        self.display.image(card, sleep_time=10)
        while True:
            card = random.randint(1, 22)
            try:
                color = random.choice(self.neo_pixel.COLORS)
                self.neo_pixel.on(0, color=color, all_on=True)
                card = 'sd/bad_advice/ba' + str(card) + '.raw'
                self.display.image(card, sleep_time=8)
                touched_left = self.touch.press(self.touch.button_left)
                touched_right = self.touch.press(self.touch.button_right)
                touched_up = self.touch.press(self.touch.button_up)
                touched_down = self.touch.press(self.touch.button_down)
                touched_submit = self.touch.press(self.touch.button_submit)
                touched_extra = self.touch.press(self.touch.button_extra)
                if touched_left or touched_right or touched_up or touched_down or touched_submit or touched_extra:
                    self.neo_pixel.clear(hard_clear=True)
                    break
            except OSError:
                # self.display.text('sd card is damaged')
                pass
