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


class BadAdvice:
    """
    Base class to handle the bad advice demo
    """

    def __init__(self, touch, display, card_bank):
        """
        Params:
            touch: object
            display: object
        """
        self.touch = touch
        self.display = display
        self.card_bank = card_bank

    def scroll(self):
        """
        Method to handle bad advice demo play
        """
        card = 'sd/bad_advice/ba1.raw'
        self.display.image(card)
        for _ in self.card_bank:
            touched = self.touch.press(self.touch.button_left)
            if touched:
                break
            card, _ = random.choice(list(self.card_bank.items()))
            try:
                card = 'sd/bad_advice/' + card
                self.display.image(card)
            except OSError:
                self.display.text('sd card is damaged')
                break
            touched = self.touch.press(self.touch.button_left)
            if touched:
                break
