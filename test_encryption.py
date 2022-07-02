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
        want = 0x10, 0x19, 0x2, 0x19, 0x4a, 0x6a, 0xc, 0xb, 0x77, 0x1c, 0x4a, 0xf, 0x10, 0xf, 0x62, 0x4a, 0x10, 0x6b, 0x19, 0x4a, 0xf, 0x10, 0x1f, 0x10, 0x17, 0x4a, 0x14, 0xb, 0x18, 0x75, 0xe, 0x4a, 0x73, 0xb, 0x4a, 0x76, 0xc, 0x19, 0x6, 0x1e, 0x1e, 0x16, 0x16, 0xf, 0x76, 0x4a, 0x19, 0x14, 0x10, 0x4a, 0x6a, 0x1c, 0x1f, 0x79, 0x17, 0x4a, 0x66, 0xc, 0xb, 0x75, 0xc, 0x23, 0x64, 0x4a, 0xb, 0x77, 0x18, 0xe, 0xc, 0x4a, 0x1d, 0xc, 0x12, 0x13, 0x24,
        got = self.encryption.cipher('d', want, 10)
        self.assertEqual(got, 'foo bar fe fo fum and a bottle of rum')


if __name__ == '__main__':
    unittest.main()
