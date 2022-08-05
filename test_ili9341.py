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

# UNITTEST
# --------
# import unittest
# unittest.main('test_ili9341')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest
from machine import Pin, SPI

from ili9341 import XglcdFont, Display


class TestDisplay(unittest.TestCase):
    """
    Test class to test ili9341 module
    """
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        display_spi = SPI(0, baudrate=40000000, sck=Pin(6, Pin.OUT), mosi=Pin(7, Pin.OUT))
        self.display = Display(display_spi, dc=Pin(15, Pin.OUT), cs=Pin(13, Pin.OUT), rst=Pin(14, Pin.OUT))
        self.UNISPACE_FONT = XglcdFont('Unispace12x24.c', 12, 24)  # load font

    def tearDown(self):
        """
        tearDown class
        """
        pass

    def test___read_reg(self):
        """
        test __read_reg functionality
        """
        # Params
        reg = 0x01
        # Returns
        return_1 = b'\x00'
        # Calls
        result = self.display.__read_reg(reg)
        # Asserts
        self.assertEqual(result, return_1)

    def test___write_reg(self):
        """
        test __write_reg functionality
        """
        # Params
        reg = self.display.RAMWR
        # Returns
        return_1 = None
        # Calls
        none_1 = self.display.__write_reg(reg)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___write_data(self):
        """
        test __write_data functionality
        """
        # Params
        data = 'foo'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.display.__write_data(data)  # noqa
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___block(self):
        """
        test __block functionality
        """
        # Params
        x0 = 1
        y0 = 2
        x1 = 3
        y1 = 4
        data = 'foo'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.display.__block(x0, y0, x1, y1, data)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_letter(self):
        """
        test letter functionality
        """
        # Params
        letter = 'a'
        color = 0b1111111111100000
        font = self.UNISPACE_FONT
        x = 1
        y = 2
        background = 0
        # Returns
        return_1 = 11
        return_2 = 24
        # Calls
        width, height = self.display.__letter(letter, color, font, x, y, background)
        # Asserts
        self.assertEqual(width, return_1)
        self.assertEqual(height, return_2)

    def test_clear(self):
        """
        test clear functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.display.clear()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_text(self):
        """
        test text functionality
        """
        # Params
        text = 'foo'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.display.text(text)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_image(self):
        """
        test image functionality
        """
        # Params
        image = 'dc540_logo.raw'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.display.image(image)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_handle_threading_setup(self):
        """
        test handle_threading_setup functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.display.handle_threading_setup()
        # Asserts
        self.assertEqual(none_1, return_1)


if __name__ == '__main__':
    unittest.main()
