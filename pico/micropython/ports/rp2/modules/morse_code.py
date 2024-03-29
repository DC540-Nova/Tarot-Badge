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

# pyright: reportMissingImports=false
# pyright: reportUndefinedVariable=false

from utime import sleep


class MorseCode:
    """
    Base class to handle morse code functionality
    """

    CODE = {
        ' ': '',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '': '..--.-'
    }

    def __init__(self, encryption, neo_pixel, color):
        """
        Params:
            encrpytion: object
            neo_pixel: object
            color: tuple
        """
        self.encryption = encryption
        self.neo_pixel = neo_pixel
        self.color = color
        self.B_RATE = 0.25

    def __dash(self):
        """
        Private method to handle morse code dash on a neo_pixel display
        """
        self.neo_pixel.on(self.color, all_on=True)
        sleep(3 * self.B_RATE)
        self.neo_pixel.clear(hard_clear=True)
        sleep(self.B_RATE)

    def __dot(self):
        """
        Private method to handle morse code dot on a neo_pixel display
        """
        self.neo_pixel.on(self.color, all_on=True)
        sleep(self.B_RATE)
        self.neo_pixel.clear(hard_clear=True)
        sleep(self.B_RATE)

    def __space(self):
        """
        Private method to handle morse code space on a neo_pixel display
        """
        self.neo_pixel.clear(hard_clear=True)
        sleep(self.B_RATE)

    def __pause(self):
        """
        Private Method to handle morse code pause on a neo_pixel display
        """
        self.neo_pixel.clear(hard_clear=True)
        sleep(7 * self.B_RATE)

    def display(self, sentence, encrypted=False):
        """
        Method to handle conversion and display of morse code

        Params:
            sentence: str
            encrypted: bool, optional
        """
        encoded_sentence = ''
        if encrypted:
            decrypted_sentence = self.encryption.cipher('d', sentence, 20)
        else:
            decrypted_sentence = sentence
        for character in decrypted_sentence:
            encoded_sentence += self.CODE[character] + ' '
        for symbol in encoded_sentence:
            if symbol == '.':
                self.__dot()
            elif symbol == '-':
                self.__dash()
            else:
                self.__pause()

    def encrypt(self, sentence):
        """
        Method to encrypt a morse code sentence

        Params:
            sentence: str

        Returns:
            str
        """
        encrypted_sentence = ''
        for letter in sentence:
            if letter != ' ':
                encrypted_sentence += self.CODE[letter] + ' '
            else:
                encrypted_sentence += ' '
        return encrypted_sentence

    def decrypt(self, encrypted_sentence):
        """
        Method to decrypt a morse code sentence

        Params:
            encrypted_sentence: str

        Returns:
            str or False
        """
        encrypted_sentence += ' '
        decrypted_sentence = ''
        character = ''
        counter = 0
        for symbol in encrypted_sentence:
            if symbol != ' ':
                counter = 0
                character += symbol
            else:
                counter += 1
                if counter == 2:
                    decrypted_sentence += ' '
                else:
                    try:
                        decrypted_sentence += list(self.CODE.keys())[list(self.CODE.values()).index(character)]
                        character = ''
                    except ValueError:
                        return False
        return decrypted_sentence
