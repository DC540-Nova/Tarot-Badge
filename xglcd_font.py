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

from math import ceil, floor


class XglcdFont(object):
    """
    Class to handle font data in X-GLCD format
    """

    # dict to tranlate bitwise values to byte position
    BIT_POS = {1: 0, 2: 2, 4: 4, 8: 6, 16: 8, 32: 10, 64: 12, 128: 14, 256: 16}

    def __init__(self, path, width, height, start_letter=32, letter_count=96):
        """
        Params:
            path: str
            width: int
            height: int
            start_letter: int, optional
            letter_count: int, optional
        """
        self.width = width
        self.height = height
        self.start_letter = start_letter
        self.letter_count = letter_count
        self.bytes_per_letter = (floor(
            (self.height - 1) / 8) + 1) * self.width + 1
        self.__load_xglcd_font(path)

    def __load_xglcd_font(self, path):
        """
        Private method to load X-GLCD font data from text file

        Parms:
            path: str
        """
        bytes_per_letter = self.bytes_per_letter
        # buffer to hold letter byte values
        self.letters = bytearray(bytes_per_letter * self.letter_count)
        mv = memoryview(self.letters)
        offset = 0
        with open(path, 'r') as f:
            for line in f:
                # skip lines that do not start with hex values
                line = line.strip()
                if len(line) == 0 or line[0:2] != '0x':
                    continue
                # remove comments
                comment = line.find('//')
                if comment != -1:
                    line = line[0:comment].strip()
                # remove trailing commas
                if line.endswith(','):
                    line = line[0:len(line) - 1]
                # convert hex strings to bytearray and insert in to letters
                mv[offset: offset + bytes_per_letter] = bytearray(
                    int(b, 16) for b in line.split(','))
                offset += bytes_per_letter

    def __lit_bits(self, n):
        """
        Private method to return positions of 1 bits only
        
        Params:
            n: int
        """
        while n:
            b = n & (~n+1)
            yield self.BIT_POS[b]
            n ^= b

    def get_letter(self, letter, color, background=0, landscape=False):
        """
        Method to convert letter byte data to pixels

        Params:
            letter: str
            color: int
            background: int, optional
            landscape: int, optional (False = portrait)
            
        Returns:
            bytearray, int, int
        """
        # get index of letter
        letter_ord = ord(letter) - self.start_letter
        # confirm font contains letter
        if letter_ord >= self.letter_count:
            print('font does not contain character: ' + letter)
            return b'', 0, 0
        bytes_per_letter = self.bytes_per_letter
        offset = letter_ord * bytes_per_letter
        mv = memoryview(self.letters[offset:offset + bytes_per_letter])
        # get width of letter (specified by first byte)
        letter_width = mv[0]
        letter_height = self.height
        # get size in bytes of specified letter
        letter_size = letter_height * letter_width
        # create buffer (double size to accommodate 16-bit colors)
        if background:
            buf = bytearray(background.to_bytes(2, 'big') * letter_size)
        else:
            buf = bytearray(letter_size * 2)
        msb, lsb = color.to_bytes(2, 'big')
        if landscape:
            # populate buffer in order for landscape
            pos = (letter_size * 2) - (letter_height * 2)
            lh = letter_height
            # loop through letter byte data and convert to pixel data
            for b in mv[1:]:
                # process only colored bits
                for bit in self.__lit_bits(b):
                    buf[bit + pos] = msb
                    buf[bit + pos + 1] = lsb
                if lh > 8:
                    # increment position by double byte
                    pos += 16
                    lh -= 8
                else:
                    # descrease position to start of previous column
                    pos -= (letter_height * 4) - (lh * 2)
                    lh = letter_height
        else:
            # populate buffer in order for portrait
            col = 0  # set column to first column
            bytes_per_letter = ceil(letter_height / 8)
            letter_byte = 0
            # loop through letter byte data and convert to pixel data
            for b in mv[1:]:
                # process only colored bits
                segment_size = letter_byte * letter_width * 16
                for bit in self.__lit_bits(b):
                    pos = (bit * letter_width) + (col * 2) + segment_size
                    buf[pos] = msb
                    pos = (bit * letter_width) + (col * 2) + 1 + segment_size
                    buf[pos] = lsb
                letter_byte += 1
                if letter_byte + 1 > bytes_per_letter:
                    col += 1
                    letter_byte = 0
        return buf, letter_width, letter_height
