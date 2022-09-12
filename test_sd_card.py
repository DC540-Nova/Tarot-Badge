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
# unittest.main('test_sd_card')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import uos
import unittest

from main import display


class TestSDCard(unittest.TestCase):
    """
    Test class to test sd_card module
    """
    def setUp(self):
        """
        setUp class
        """
        self.display = display

    @staticmethod
    def tearDown():
        """
        tearDown class
        """
        # Remove temp file
        try:
            uos.remove('sd/temp')
        except OSError:
            pass

    def test_read(self):
        """
        test read functionality
        """
        # Params
        path = 'sd/Rider-Waite/00-TheFool.raw'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.display.image(path)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_write(self):
        """
        test write functionality
        """
        # Params
        path = 'sd/temp'
        write_operation = 'w'
        read_operation = 'r'
        text = 'foo'
        foo = ''  # noqa
        # Returns
        return_1 = 'foo'
        # Calls
        with open(path, write_operation) as f:
            f.write(text)
        with open(path, read_operation) as f:
            foo = f.read()
        # Asserts
        self.assertEqual(foo, return_1)
