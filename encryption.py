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

from ucryptolib import aes


class Encryption:
    """
    Method to handle encryption
    """

    def __init__(self):
        self.mode = 1

    def encode(self, decrypted_message):
        """
        Method to handle encoding a message

        Params:
            decrypted_message: str

        Return:
            bytes
        """
        encrypt = aes(b'2905386475820143', self.mode)
        encrypt_bytes = decrypted_message.encode()
        encrypted_message = encrypt.encrypt(encrypt_bytes + b'\x00' * ((16 - (len(encrypt_bytes) % 16)) % 16))
        return encrypted_message

    def decode(self, encrypted_message):
        """
        Method to handle decoding a message

        Params:
            encrypted_message: bytes

        Return:
            str
        """
        decrypt = aes(b'2905386475820143', self.mode)
        decrypted_message = decrypt.decrypt(encrypted_message)
        decrypted_message = str(decrypted_message)
        decrypted_message = decrypted_message.split('\\')
        decrypted_message = decrypted_message[0][2:]
        return decrypted_message
