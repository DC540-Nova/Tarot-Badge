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

from math import ceil, floor
import utime
import ustruct
import gc
from machine import Pin
from micropython import const


class XglcdFont:
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
            b = n & (~n + 1)
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
            # print('font does not contain character: ' + letter)
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


class Display:
    """
    Class to handle IL9341 display
    """

    # ili9341 registers & commands
    NOP = const(0x00)
    SWRESET = const(0x01)
    RDDIDIF = const(0x04)
    RDDST = const(0x09)
    RDDPM = const(0x0a)
    RDDMADCTL = const(0x0b)
    RDDCOLMOD = const(0x0c)
    RDDIM = const(0x0d)
    RDDSM = const(0x0e)
    RDDSDR = const(0x0f)
    SLPIN = const(0x10)
    SLPOUT = const(0x11)
    PTLON = const(0x12)
    NORON = const(0x13)
    DINVOFF = const(0x20)
    DINVON = const(0x21)
    GAMSET = const(0x26)
    DISPOFF = const(0x28)
    DISPON = const(0x29)
    CASET = const(0x2a)
    PASET = const(0x2b)
    RAMWR = const(0x2c)
    RGBSET = const(0x2d)
    RAMRD = const(0x2e)
    PTLAR = const(0x30)
    VSCRDEF = const(0x33)
    TEOFF = const(0x34)
    TEON = const(0x35)
    MADCTL = const(0x36)
    VSCRSADD = const(0x37)
    IDMOFF = const(0x38)
    IDMON = const(0x39)
    PIXSET = const(0x3a)
    WRITE_MEMORY_CONTINUE = const(0x3c)
    READ_MEMORY_CONTINUE = const(0x3e)
    SET_TEAR_SCANLINE = const(0x44)
    GET_SCANLINE = const(0x45)
    WRDISBV = const(0x51)
    RDDISBV = const(0x52)
    WRCTRLD = const(0x53)
    RDCTRLD = const(0x54)
    WRCABC = const(0x55)
    RDCABC = const(0x56)
    WRITE_CABC_MINIMUM_BRIGHTNESS = const(0x5e)
    READ_CABC_MINIMUM_BRIGHTNESS = const(0x5f)
    RDID1 = const(0xda)
    RDID2 = const(0xdb)
    RDID3 = const(0xdc)
    IFMODE = const(0xb0)
    FRMCTR1 = const(0xb1)
    FRMCTR2 = const(0xb2)
    FRMCTR3 = const(0xb3)
    INVTR = const(0xb4)
    PRCTR = const(0xb5)
    DISCTRL = const(0xb6)
    ETMOD = const(0xb7)
    BACKLIGHT_CONTROL_1 = const(0xb8)
    BACKLIGHT_CONTROL_2 = const(0xb9)
    BACKLIGHT_CONTROL_3 = const(0xba)
    BACKLIGHT_CONTROL_4 = const(0xbb)
    BACKLIGHT_CONTROL_5 = const(0xbc)
    BACKLIGHT_CONTROL_7 = const(0xbe)
    BACKLIGHT_CONTROL_8 = const(0xbf)
    PWCTRL1 = const(0xc0)
    PWCTRL2 = const(0xc1)
    VMCTRL1 = const(0xc5)
    VMCTRL2 = const(0xc7)
    NVMWR = const(0xd0)
    NVMPKEY = const(0xd1)
    RDNVM = const(0xd2)
    RDID4 = const(0xd3)
    PGAMCTRL = const(0xe0)
    NGAMCTRL = const(0xe1)
    DGAMCTRL1 = const(0xe2)
    DGAMCTRL2 = const(0xe3)
    IFCTL = const(0xf6)
    POWER_CONTROL_A = const(0xcb)
    POWER_CONTROL_B = const(0xcf)
    DRIVER_TIMING_CONTROL_A1 = const(0xe8)
    DRIVER_TIMING_CONTROL_A2 = const(0xe9)
    DRIVER_TIMING_CONTROL_B = const(0xea)
    POWER_ON_SEQUENCE_CONTROL = const(0xed)
    ENABLE_3G = const(0xf2)
    PUMP_RATIO_CONTROL = const(0xf7)

    # fonts
    UNISPACE_FONT = XglcdFont('Unispace12x24.c', 12, 24)  # load font

    # led pin
    POWER_DISPLAY = Pin(2, Pin.OUT)  # init led pin

    ROTATE = {
        0: 0x88,
        90: 0xE8,
        180: 0x48,
        270: 0x28
    }

    def __init__(self, spi, cs, dc, rst, width=240, height=320, rotation=0):
        """
        Params:
            spi: object
            cs: object
            dc: object
            rst: object
            width: int, optional
            height: int, optional
            rotation: int, optional
        """
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.width = width
        self.height = height
        if rotation not in self.ROTATE.keys():
            raise RuntimeError('rotation must be 0, 90, 180 or 270')
        else:
            self.rotation = self.ROTATE[rotation]
        self.__config()

    def __config(self):
        """
        Private method to handle config
        """
        self.cs.init(self.cs.OUT, value=1)
        self.dc.init(self.dc.OUT, value=0)
        self.rst.init(self.rst.OUT, value=1)
        self.__write_reg(self.SWRESET)  # software reset
        utime.sleep(.1)
        self.__write_reg(self.POWER_CONTROL_B, 0x00, 0xc1, 0x30)  # 1,2,3 param values given in datasheet
        self.__write_reg(self.POWER_ON_SEQUENCE_CONTROL, 0x64, 0x03, 0x12, 0x81)  # 1: soft start ctrl, 2,3: power on seq ctrl, 4: DDVDH enhance mode  # noqa
        self.__write_reg(self.DRIVER_TIMING_CONTROL_A1, 0x85, 0x00, 0x78)  # 1: gate driver non-overlap timing control, 2: EQ timing control, 3: pre-charge timing control  # noqa
        self.__write_reg(self.POWER_CONTROL_A, 0x39, 0x2c, 0x00, 0x34, 0x02)  # 1,2,3,4,5 param values given in datasheet  # noqa
        self.__write_reg(self.PUMP_RATIO_CONTROL, 0x20)  # 1: ratio control
        self.__write_reg(self.DRIVER_TIMING_CONTROL_B, 0x00, 0x00)  # 1: gate driver timing control, 2: param value given in datasheet  # noqa
        self.__write_reg(self.PWCTRL1, 0x23)  # 1: set the GVDD level
        self.__write_reg(self.PWCTRL2, 0x10)  # 1 param value given in datasheet
        self.__write_reg(self.VMCTRL1, 0x3e, 0x28)  # 1: set the VCOMH voltage, 2: set the VCOML voltage
        self.__write_reg(self.VMCTRL2, 0x86)  # 1: set the VCOM offset voltage
        self.__write_reg(self.MADCTL, self.rotation)
        self.__write_reg(self.VSCRSADD, 0x00)  # 1 param value given in datasheet
        self.__write_reg(self.PIXSET, 0x55)  # 1: set the pixel format for the RGB image data used by the interface
        self.__write_reg(self.FRMCTR1, 0x00, 0x18)  # 1 param value given in datasheet, 2: division ratio for internal clocks when Normal mode  # noqa
        self.__write_reg(self.DISCTRL, 0x08, 0x82, 0x27)  # 1,2,3 param values given in datasheet
        self.__write_reg(self.ENABLE_3G, 0x00)  # 1: enable 3 gamma control
        self.__write_reg(self.GAMSET, 0x01)  # 1 param value given in datasheet
        self.__write_reg(self.PGAMCTRL, 0x0f, 0x31, 0x2b, 0x0c, 0x0e, 0x08, 0x4e, 0xf1, 0x37, 0x07, 0x10, 0x03, 0x0e, 0x09, 0x00)  # params set the gray scale voltage to adjust the gamma characteristics of the TFT panel  # noqa
        self.__write_reg(self.NGAMCTRL, 0x00, 0x0e, 0x14, 0x03, 0x11, 0x07, 0x31, 0xc1, 0x48, 0x08, 0x0f, 0x0c, 0x31, 0x36, 0x0f)  # params set the gray scale voltage to adjust the gamma characteristics of the TFT panel  # noqa
        self.__write_reg(self.SLPOUT)  # sleep out
        utime.sleep(.1)
        self.__write_reg(self.DISPON)  # display on
        utime.sleep(.1)
        self.clear()

    def __read_reg(self, reg, size=1, debug=False):
        """
        Private method to read a register

        Params:
            reg: int
            size: int, optional
            debug: bool, optional

        Returns:
            object
        """
        self.cs(0)
        self.spi.write(bytearray([reg]))
        result = self.spi.read(size)
        self.cs(1)
        if debug:
            print([bin(value) for value in result])
        return result

    def __write_reg(self, reg, *args):
        """
        Private method to write to a register

        Params:
            reg: int
            *args: bytes, optional
        """
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([reg]))
        self.cs(1)
        # handle any passed data
        if len(args) > 0:
            self.__write_data(bytearray(args))

    def __write_data(self, data):
        """
        Private method to write data to display

        Params:
            data: bytes
        """
        self.dc(1)
        self.cs(0)
        self.spi.write(data)
        self.cs(1)

    def __block(self, x0, y0, x1, y1, data):
        """
        Private method to write a block of data to display

        Params:
            x0: int
            y0: int
            x1: int
            y1: int
            data: bytes
        """
        self.__write_reg(self.CASET, *ustruct.pack('>HH', x0, x1))
        self.__write_reg(self.PASET, *ustruct.pack('>HH', y0, y1))
        self.__write_reg(self.RAMWR)
        self.__write_data(data)

    def __letter(self, letter, color, font, x, y, background=0):
        """
        Private method to draw a single letter

        Params:
            letter: str
            color: int
            font: object
            x: int
            y: int
            background: int, optional

        Returns:
            int, int
        """
        buf, width, height = font.get_letter(letter, color, background)
        self.__block(x, y, x + width - 1, y + height - 1, buf)
        return width, height
    
    def clear(self, color=0):
        """
        Method to clear display

        Params:
            color: int, optional
        """
        width = self.width
        height = self.height
        # clear display in 1024 byte blocks
        if color:
            line = color.to_bytes(2, 'big') * (width * 8)
        else:
            line = bytearray(width * 16)
        for y in range(0, height, 8):
            self.__block(0, y, width - 1, y + 7, line)

    def text(self, text, x=8, y=0, color=0b1111111111100000, font=UNISPACE_FONT, wrap=True, clear=True, sleep_time=6,
             timed=True, off=False):
        """
        Method to draw text

        Params:
            text: str
            x: int, optional
            y: int, optional
            color: int, optional
            font: object, optional
            wrap: bool, optional
            clear: bool, optional
            sleep_time: int, optional
            timed: bool, optional
            off: bool, optional
        """
        if clear:
            self.POWER_DISPLAY.value(0)
            self.rotation = self.ROTATE[0]
            self.__config()
        spacing = 1
        background = 0
        if wrap:
            for letter in text:
                if letter == ' ' and x > 100:  # wrap text as good as possible
                    x = 0
                    y += 24
                width, height = self.__letter(letter, color, font, x, y, background)  # get letter array and letter dimension  # noqa
                x += (width + spacing)
        else:
            for letter in text:
                width, height = self.__letter(letter, color, font, x, y, background)  # get letter array and letter dimension  # noqa
                x += (width + spacing)
        if not off:
            self.POWER_DISPLAY.value(1)
        if timed:
            utime.sleep(sleep_time)
            self.POWER_DISPLAY.value(0)

    def image(self, path, sleep_time=2, up=True, timed=True, multithreading=False):
        """
        Method to draw image on display

        Params:
            path: str
            sleep_time: int, optional
            up: bool, optional
            timed: bool, optional
            multithreading: bool, optional
        """
        self.POWER_DISPLAY.value(0)
        x = 0
        y = 0
        width = 240
        height = 320
        draw_speed = 512
        if up:
            self.rotation = self.ROTATE[0]
            self.__config()
        if not up:
            self.rotation = self.ROTATE[180]
            self.__config()
        if not multithreading:
            self.clear()
        x2 = x + width - 1
        with open(path, 'rb') as f:
            gc.collect()
            chunk_height = draw_speed // width  # 153600 total bytes of an image
            chunk_count, remainder = divmod(height, chunk_height)
            chunk_size = chunk_height * width * 2
            chunk_y = y
            if chunk_count:
                for _ in range(0, chunk_count):
                    gc.collect()
                    buf = f.read(chunk_size)
                    self.__block(x, chunk_y, x2, chunk_y + chunk_height - 1, buf)
                    chunk_y += chunk_height
            if remainder:
                gc.collect()
                buf = f.read(remainder * width * 2)
                self.__block(x, chunk_y, x2, chunk_y + remainder - 1, buf)
        if not multithreading:
            self.POWER_DISPLAY.value(1)
            if timed:
                utime.sleep(sleep_time)
                self.POWER_DISPLAY.value(0)

    def handle_threading_setup(self):
        """
        Method to handle threading setup functionality to ensure thread does not crash
        """
        self.clear()
