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

from utime import sleep

from config import neo_pixel, RED
import encryption

# TODO: make a class

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

B_RATE = 0.25


def dash(color=RED):
    """
    Function to handle morse code dash on a neo_pixel display

    Params:
        color: int, optional
    """
    neo_pixel.on(color, all_on=True)
    sleep(3 * B_RATE)
    neo_pixel.clear(hard_clear=True)
    sleep(B_RATE)


def dot(color=RED):
    """
    Function to handle morse code dot on a neo_pixel display

    Params:
        color: tuple, optional
    """
    neo_pixel.on(color, all_on=True)
    sleep(B_RATE)
    neo_pixel.clear(hard_clear=True)
    sleep(B_RATE)


def space():
    """
    Function to handle morse code space on a neo_pixel display
    """
    neo_pixel.clear(hard_clear=True)
    sleep(B_RATE)


def pause():
    """
    Function to handle morse code pause on a neo_pixel display
    """
    neo_pixel.clear(hard_clear=True)
    sleep(7 * B_RATE)


def display(sentence, color=RED, encrypted=False):
    """
    Function to handle conversion and display of morse code

    Params:
        sentence: str
        color: tuple, optional
        encrypted: bool, optional
    """
    encoded_sentence = ''
    if encrypted:
        decrypted_sentence = encryption.cipher('d', sentence, 22)
    else:
        decrypted_sentence = sentence
    for character in decrypted_sentence:
        encoded_sentence += CODE[character] + ' '
    for letter in encoded_sentence:
        if letter == '.':
            dot(color)
        elif letter == '-':
            dash(color)
        else:
            pause()
