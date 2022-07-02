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

from random import randint


class Encryption:
    """
    Method to handle encryption
    """

    def __init__(self):
        self.enigma = None

    def __random_number_generator(self):
        """
        Random number generator method which takes a number between 0x0000 and 0xFFFF inclusive
        and outputs a new number between 0x0000 and 0xFFFF inclusive to which this will always
        return the same output for a given input where each output is derived from exactly
        1 input, and you can repeatedly feed in the output again to get a new number and
        with the same starting number, you will always get the same pseudo-random sequence and
        this can be repeated 65,536 times before a number is output again

        Returns:
            int
        """
        io = abs(self.enigma)
        if io > 0xFFFF:
            io = io % 0x10000
        # ex: with input of 0xDEAF (1101111010101111)
        # s0 = 0xDEAF00 (110111101010111100000000)
        s0 = io << 8
        # s0 = 0xAF00 (1010111100000000)
        s0 = s0 % 0x10000
        # s0 = 0x71AF (0111000110101111) XOR bitwise operation
        s0 = s0 ^ io
        # io = 0xAF71 (1010111101110001) Swaps bytes
        io = ((s0 % 0x100) * 0x100) + (s0 // 0x100)
        # takes the right byte of s0 (0x00AF 0000000010101111)
        s0_right_byte = s0 % 0x100
        # bitwise shifts by 1 digit (0x015E 0000000101011110)
        s0_shifted_right_byte = s0_right_byte << 1
        # XORs it with input to get (0xAE2F 1010111000101111)
        s0 = io ^ s0_shifted_right_byte
        constant = 0xFF80
        # bitwise shifts by 1 digit to the right
        # s0 becomes (0x5717 0101011100010111)
        # then XOR with constant
        # s1 becomes (0xA897 1010100010010111)
        s1 = (s0 >> 1) ^ constant
        if s0 % 0x2 == 1:
            constant = 0x8180  # 1000000110000000
        else:
            constant = 0x1ff4  # 0001111111110100
        # s1 ^ 0x8180 becomes (0x2917 0010100100010111)
        io = s1 ^ constant
        return io

    def cipher(self, mode, message, key):
        """
        Cipher method to encrypt and decrypt messages where the encryption steps include
        a shift to every character by the magnitude of key, add additional characters
        and "enigmafy" message using the key again and the decryption steps include
        "de-enigmafy" the message using key, remove added characters and un-shift every
        character by magnitude of key

        Params:
            mode: str
            message: str
            key: int

        Returns:
            str
        """
        shifted_message = ''
        salted_message = ''
        encrypted_message = ''
        un_shifted_message = ''
        unsalted_message = ''
        decrypted_message = ''
        hex_encrypted_message = ''
        hex_decrypted_message = ''
        message_length = len(message)
        self.enigma = key * key * 42  # Initial enigma value
        if mode[0] == 'e':
            # shift message
            for _ in message:
                num = ord(_)
                num += key
                num = num % 128
                shifted_message += chr(num)
            # salt message
            # for long messages
            if len(shifted_message) > 8:
                while len(shifted_message) > 3:
                    # separate first 3 chars of message
                    fragment = shifted_message[0:2]
                    # the shifted_message is now the remainder
                    shifted_message = shifted_message[2:]
                    # randomly chooses A-Z or a-z
                    coin = randint(1, 2)
                    if coin == 1:
                        rand_char = chr(randint(65, 90))
                    else:
                        rand_char = chr(randint(97, 122))
                    # build salted_message
                    salted_message += fragment + rand_char
                # add whatever part of the shifted_message remains
                salted_message += shifted_message
            # for short messages
            else:
                coin = randint(1, 2)
                if coin == 1:
                    rand_char = chr(randint(65, 90))
                else:
                    rand_char = chr(randint(97, 122))
                salted_message += rand_char + shifted_message + rand_char
            # enigma message
            for _ in salted_message:
                # increment enigma
                enigma = self.__random_number_generator()
                num = ord(_)
                num += enigma
                num = num % 128
                encrypted_message += chr(num)
            # convert encrypted_message from chars to hex bytes
            for _ in encrypted_message:
                hex_encrypted_message += hex(ord(_)) + ', '
            return hex_encrypted_message
        if mode[0] == 'd':
            # convert message from hex bytes to chars
            for _ in message:
                hex_decrypted_message += chr(_)
            # de-enigma message
            for _ in hex_decrypted_message:
                # increment enigma
                enigma = self.__random_number_generator()
                num = ord(_)
                num -= enigma
                num = num % 128
                salted_message += chr(num)
            # un-salt message
            if len(salted_message) > 8:
                while len(salted_message) > 4:
                    unsalted_message += salted_message[0:2]
                    salted_message = salted_message[3:]
            else:
                unsalted_message = salted_message[1:-1]
            unsalted_message += salted_message
            # un-shift message
            for _ in unsalted_message:
                num = ord(_)
                num -= key
                if num < 0:
                    num += 128
                un_shifted_message += chr(num)
                decrypted_message = un_shifted_message
            if message_length == 1 or message_length == 5:
                return decrypted_message[:int((message_length / 2) + 1)]
            else:
                return decrypted_message[:int(message_length / 2)]
