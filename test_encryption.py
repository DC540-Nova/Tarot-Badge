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
        # Params
        mode = 'd'
        message = 0xd, 0x10, 0xd,
        key = 10
        # Returns
        return_1 = 'f'
        # Calls
        encrypted_message = self.encryption.cipher(mode, message, key)
        self.assertEqual(encrypted_message, return_1)

    def test_decryption_medium_length_word(self):
        """
        test decryption medium length word functionality
        """
        # Params
        mode = 'd'
        message = 0x71, 0x10, 0x19, 0x71,
        key = 10
        # Returns
        return_1 = 'fo'
        # Calls
        decrypted_message = self.encryption.cipher(mode, message, key)
        # Asserts
        self.assertEqual(decrypted_message, return_1)

    def test_decryption_large_length_word(self):
        """
        test decryption large length word functionality
        """
        # Params
        mode = 'd'
        message = 0x9, 0x10, 0x19, 0x19, 0x9,
        key = 10
        # Returns
        return_1 = 'foo'
        # Calls
        decrypted_message = self.encryption.cipher(mode, message, key)
        # Asserts
        self.assertEqual(decrypted_message, return_1)

    def test_decryption_extra_large_length_word(self):
        """
        test decryption extra large length word functionality
        """
        # Params
        mode = 'd'
        message = 0x10, 0x19, 0x14, 0x19, 0x4a, 0x9, 0xc, 0xb, 0x63, 0x1c, 0x4a, 0xf, 0x10, 0xf, 0x75, 0x4a, 0x10, 0x13, 0x19, 0x4a, 0x6, 0x10, 0x1f, 0x14, 0x17, 0x4a, 0x15, 0xb, 0x18, 0x11, 0xe, 0x4a, 0x3, 0xb, 0x4a, 0x1, 0xc, 0x19, 0x61, 0x1e, 0x1e, 0xc, 0x16, 0xf,  # noqa
        key = 10
        # Returns
        return_1 = 'foo bar fe fo fum and '
        # Calls
        decrypted_message = self.encryption.cipher(mode, message, key)
        # Asserts
        self.assertEqual(decrypted_message, return_1)

    def test_encryption_over_length_word(self):
        """
        test encryption over length word functionality
        """
        # Params
        mode = 'e'
        message = 'message must be less than 38 chars'
        key = 10
        # Returns
        return_1 = 'message must be less than 38 chars'
        # Calls
        decrypted_message = self.encryption.cipher(mode, message, key)
        self.assertEqual(decrypted_message, return_1)

    def test_decryption_over_length_word(self):
        """
        test decryption over length word functionality
        """
        # Params
        mode = 'd'
        message = 0x10, 0x19, 0x14, 0x19, 0x4a, 0x9, 0xc, 0xb, 0x63, 0x1c, 0x4a, 0xf, 0x10, 0xf, 0x75, 0x4a, 0x10, 0x13, 0x19, 0x4a, 0x6, 0x10, 0x1f, 0x14, 0x17, 0x4a, 0x15, 0xb, 0x18, 0x11, 0xe, 0x4a, 0x3, 0xb, 0x4a, 0x1, 0xc, 0x19, 0x61, 0x1e, 0x1e, 0xc, 0x16, 0xf, 0x61, 0x1e, 0x1e, 0xc, 0x16,  # noqa
        key = 10
        # Returns
        return_1 = 'message must be less than 44 chars'
        # Calls
        decrypted_message = self.encryption.cipher(mode, message, key)
        self.assertEqual(decrypted_message, return_1)


if __name__ == '__main__':
    unittest.main()
