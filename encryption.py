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


def __random_number_generator(io):
    """
    Random number generator method which takes a number between 0x0000 and 0xFFFF inclusive
    and outputs a new number between 0x0000 and 0xFFFF inclusive to which this will always
    return the same output for a given input where each output is derived from exactly
    1 input, and you can repeatedly feed in the output again to get a new number and
    with the same starting number, you will always get the same pseudo-random sequence and
    this can be repeated 65,536 times before a number is output again

    Params:
        io: int
    Returns:
        int
    """
    io = abs(io)
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


def cipher(m_mode, m_message, m_key):
    """
    Cipher method to encrypt and decrypt messages where the encryption steps include
    a shift to every character by the magnitude of key, add additional characters
    and "enigmafy" message using the key again and the decryption steps include
    "de-enigmafy" the message using key, remove added characters and un-shift every
    character by magnitude of -key

    Params:
        m_mode: str
        m_message: str
        m_key: int

    Returns:
        str
    """
    m_shifted_message = ''
    m_salted_message = ''
    m_encrypted_message = ''
    m_un_shifted_message = ''
    m_unsalted_message = ''
    m_decrypted_message = ''
    m_hex_encrypted_message = ''
    m_hex_decrypted_message = ''
    m_enigma = m_key * m_key * 42  # Initial enigma value
    if m_mode[0] == 'e':
        # shift message
        for _ in m_message:
            num = ord(_)
            num += m_key
            num = num % 128
            m_shifted_message += chr(num)
        # salt message
        # for long messages
        if len(m_shifted_message) > 8:
            while len(m_shifted_message) > 3:
                # separate first 3 chars of message
                fragment = m_shifted_message[0:2]
                # the m_shifted_message is now the remainder
                m_shifted_message = m_shifted_message[2:]
                # randomly chooses A-Z or a-z
                coin = randint(1, 2)
                if coin == 1:
                    rand_char = chr(randint(65, 90))
                else:
                    rand_char = chr(randint(97, 122))
                # build m_salted_message
                m_salted_message += fragment + rand_char
            # add whatever part of the m_shifted_message remains
            m_salted_message += m_shifted_message
        # for short messages
        else:
            coin = randint(1, 2)
            if coin == 1:
                rand_char = chr(randint(65, 90))
            else:
                rand_char = chr(randint(97, 122))
            m_salted_message += rand_char + m_shifted_message + rand_char
        # enigma message
        for _ in m_salted_message:
            # increment enigma
            m_enigma = __random_number_generator(m_enigma)
            num = ord(_)
            num += m_enigma
            num = num % 128
            m_encrypted_message += chr(num)
        # convert m_encrypted_message from chars to hex bytes
        for _ in m_encrypted_message:
            m_hex_encrypted_message += hex(ord(_)) + ', '
        return m_hex_encrypted_message
    if m_mode[0] == 'd':
        # convert m_message from hex bytes to chars
        for _ in m_message:
            m_hex_decrypted_message += chr(_)
        # de-enigma message
        for _ in m_hex_decrypted_message:
            # increment enigma
            m_enigma = __random_number_generator(m_enigma)
            num = ord(_)
            num -= m_enigma
            num = num % 128
            m_salted_message += chr(num)
        # un-salt message
        if len(m_salted_message) > 8:
            while len(m_salted_message) > 4:
                m_unsalted_message += m_salted_message[0:2]
                m_salted_message = m_salted_message[3:]
        else:
            m_unsalted_message = m_salted_message[1:-1]
        m_unsalted_message += m_salted_message
        # un-shift message
        for _ in m_unsalted_message:
            num = ord(_)
            num -= m_key
            if num < 0:
                num += 128
            m_un_shifted_message += chr(num)
            m_decrypted_message = m_un_shifted_message
        return m_decrypted_message
