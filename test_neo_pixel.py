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
# unittest.main('test_neo_pixel')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest
from machine import Pin

from neo_pixel import NeoPixel


class TestMicrocontroller(unittest.TestCase):
    """
    Test class to test microcontroller module
    """
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        LED_PIN = 5
        LED_COUNT = 32
        from neo_pixel import NeoPixel  # noqa
        self.neo_pixel = NeoPixel(Pin, LED_PIN, LED_COUNT)

    def tearDown(self):
        """
        tearDown class
        """
        # Clear leds
        self.neo_pixel.clear(hard_clear=True)

    def test___set(self):
        """
        test __set functionality
        """
        # Params
        led = 0
        color = self.neo_pixel.BLACK
        # Returns
        return_1 = None
        # Calls
        none_1 = self.neo_pixel.__set(led, color)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___show(self):
        """
        test __show functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.neo_pixel.__show()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_clear(self):
        """
        test clear functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.neo_pixel.clear()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_on(self):
        """
        test on functionality
        """
        # Params:
        led = 0
        # Returns
        return_1 = None
        # Calls
        none_1 = self.neo_pixel.on(led)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_off(self):
        """
        test off functionality
        """
        # Params:
        led = 0
        # Returns
        return_1 = None
        # Calls
        none_1 = self.neo_pixel.off(led)
        # Asserts
        self.assertEqual(none_1, return_1)
