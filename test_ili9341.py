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
        display_spi = SPI(0, baudrate=40000000, sck=Pin(6, Pin.OUT), mosi=Pin(7, Pin.OUT))
        self.display = Display(display_spi, dc=Pin(15, Pin.OUT), cs=Pin(13, Pin.OUT), rst=Pin(14, Pin.OUT))
        self.UNISPACE_FONT = XglcdFont('Unispace12x24.c', 12, 24)  # load font

    def tearDown(self):
        """
        tearDown class
        """
        pass

    def test_read_reg(self):
        """
        test read_reg functionality
        """
        want = b'\x00'
        got = self.display.__read_reg(0x01)  # noqa
        self.assertEqual(got, want)

    def test_write_reg(self):
        """
        test write_reg functionality
        """
        want = None
        got = self.display.__write_reg(self.display.RAMWR)  # noqa
        self.assertEqual(got, want)

    def test_write_data(self):
        """
        test write_data functionality
        """
        want = None
        got = self.display.__write_data('foo')  # noqa
        self.assertEqual(got, want)

    def test_block(self):
        """
        test block functionality
        """
        want = None
        got = self.display.__block(1, 2, 3, 4, 'foo')  # noqa
        self.assertEqual(got, want)

    def test_letter(self):
        """
        test letter functionality
        """
        want_width = 11
        want_height = 24
        got_width, got_height = self.display.__letter('a', 0b1111111111100000, self.UNISPACE_FONT, 1, 2, 0)  # noqa
        self.assertEqual(got_width, want_width)
        self.assertEqual(got_height, want_height)

    def test_clear(self):
        """
        test clear functionality
        """
        want = None
        got = self.display.clear()
        self.assertEqual(got, want)

    def test_text(self):
        """
        test text functionality
        """
        want = None
        got = self.display.text('foo')
        self.assertEqual(got, want)

    def test_image(self):
        """
        test image functionality
        """
        want = None
        got = self.display.image('dc540_logo.raw')
        self.assertEqual(got, want)

    def test_handle_threading_setup(self):
        """
        test handle_threading_setup functionality
        """
        want = None
        got = self.display.handle_threading_setup()
        self.assertEqual(got, want)

    def test_handle_threading_teardown(self):
        """
        test handle_threading_teardown functionality
        """
        want = None
        got = self.display.handle_threading_teardown()
        self.assertEqual(got, want)


if __name__ == '__main__':
    unittest.main()
