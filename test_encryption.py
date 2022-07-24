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
        # Instantiate
        self.encryption = Encryption()

    def tearDown(self):
        """
        tearDown class
        """
        pass

    def test_encode(self):
        """
        test encode functionality
        """
        # Params
        decrypted_message = 'foo bar'
        # Returns
        return_1 = b'\xd4\xb5\x86c\xc4\xec\xa5\xe0\x03Y\xaaz\xe4\xf2\x90\xe5'
        # Calls
        encrypted_message = self.encryption.encode(decrypted_message)
        # Asserts
        self.assertEqual(encrypted_message, return_1)

    def test_decode(self):
        """
        test decode functionality
        """
        # Params
        encrypted_message = b'\xd4\xb5\x86c\xc4\xec\xa5\xe0\x03Y\xaaz\xe4\xf2\x90\xe5'
        # Returns
        return_1 = 'foo bar'
        # Calls
        decrypted_message = self.encryption.decode(encrypted_message)
        # Asserts
        self.assertEqual(decrypted_message, return_1)


if __name__ == '__main__':
    unittest.main()
