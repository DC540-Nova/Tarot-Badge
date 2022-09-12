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
# unittest.main('test_morse_code')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from main import neo_pixel
from encryption import Encryption
encryption = Encryption()
from morse_code import MorseCode


class TestMorseCode(unittest.TestCase):
    """
    Test class to test morse_code module
    """
    def setUp(self):
        """
        setUp class
        """
        # Instantiate
        self.morse_code = MorseCode(encryption, neo_pixel, neo_pixel.RED)

    def tearDown(self):
        """
        tearDown class
        """
        pass

    def test___dash(self):
        """
        test __dash functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.morse_code.__dash()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___dot(self):
        """
        test __dot functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.morse_code.__dot()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___space(self):
        """
        test __space functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.morse_code.__space()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test___pause(self):
        """
        test __pause functionality
        """
        # Returns
        return_1 = None
        # Calls
        none_1 = self.morse_code.__pause()
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_display(self):
        """
        test display functionality
        """
        # Params
        sentence = 'SOS'
        # Returns
        return_1 = None
        # Calls
        none_1 = self.morse_code.display(sentence)
        # Asserts
        self.assertEqual(none_1, return_1)

    def test_encrypt(self):
        """
        test encrypt functionality
        """
        # Params
        sentence = 'SOS'
        # Returns
        return_1 = '... --- ... '
        # Calls
        encrypted_sentence = self.morse_code.encrypt(sentence)
        # Asserts
        self.assertEqual(encrypted_sentence, return_1)

    def test_decrypt(self):
        """
        test decrypt functionality
        """
        # Params
        encrypted_sentence = '... --- ...'
        # Returns
        return_1 = 'SOS'
        # Calls
        encrypted_sentence = self.morse_code.decrypt(encrypted_sentence)
        # Asserts
        self.assertEqual(encrypted_sentence, return_1)

    def test_decrypt_invalid_input(self):
        """
        test decrypt invalid input functionality
        """
        # Params
        encrypted_sentence = 'foo'
        # Returns
        return_1 = False
        # Calls
        encrypted_sentence = self.morse_code.decrypt(encrypted_sentence)
        # Asserts
        self.assertEqual(encrypted_sentence, return_1)
