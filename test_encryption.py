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
# unittest.main('test_encryption')

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

import unittest

from encryption import Encryption


class TestEncryption(unittest.TestCase):
    """
    Test class to test encryption module
    """
    def setUp(self):
        """
        setUp class
        """
        self.encryption = Encryption()

    def tearDown(self):
        """
        tearDown class
        """
        pass

    def test_encryption_over_length_word(self):
        """
        test encryption over length word functionality
        """
        want = 'message must be less than 38 chars'
        got = self.encryption.cipher('e', want, 10)
        self.assertEqual(got, want)

    def test_decryption_small_length_word(self):
        """
        test decryption small length word functionality
        """
        want = 0xd, 0x10, 0xd,
        got = self.encryption.cipher('d', want, 10)
        self.assertEqual(got, 'f')

    def test_decryption_medium_length_word(self):
        """
        test decryption medium length word functionality
        """
        want = 0x71, 0x10, 0x19, 0x71,
        got = self.encryption.cipher('d', want, 10)
        self.assertEqual(got, 'fo')

    def test_decryption_large_length_word(self):
        """
        test decryption large length word functionality
        """
        want = 0x9, 0x10, 0x19, 0x19, 0x9,
        got = self.encryption.cipher('d', want, 10)
        self.assertEqual(got, 'foo')

    def test_decryption_extra_large_length_word(self):
        """
        test decryption extra large length word functionality
        """
        want = 0x10, 0x19, 0x15, 0x19, 0x4a, 0x12, 0xc, 0xb, 0x73, 0x1c, 0x4a, 0xe, 0x10, 0xf, 0x6b, 0x4a, 0x10, 0x68, 0x19, 0x4a, 0x1a, 0x10, 0x1f, 0x77, 0x17, 0x4a, 0x79, 0xb, 0x18, 0xb, 0xe, 0x4a, 0x65, 0xb, 0x4a, 0x17, 0xc, 0x19, 0x62, 0x1e, 0x1e, 0x70, 0x16, 0xf, 0xc, 0x4a, 0x19, 0x10,  # noqa
        got = self.encryption.cipher('d', want, 10)
        self.assertEqual(got, 'foo bar fe fo fum and a bottle of')

    def test_decryption_over_length_word(self):
        """
        test decryption over length word functionality
        """
        want = 'message must be less than 34 chars'
        got = self.encryption.cipher('d', want, 10)
        self.assertEqual(got, want)


if __name__ == '__main__':
    unittest.main()
