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

import utime
import ustruct
import gc
from machine import Pin
from micropython import const

from xglcd_font import XglcdFont


class Display:
    """
    Class to handle IL9341 display
    """

    # ili9341 registers
    NOP = const(0x00)  # NOP p. 89
    SWRESET = const(0x01)  # Software Reset p. 90
    RDDIDIF = const(0x04)  # Read Display Identification Information p. 91
    RDDST = const(0x09)  # Read Display Status p. 92
    RDDPM = const(0x0a)  # Read Display Power Mode p. 94
    RDDMADCTL = const(0x0b)  # Read Display MADCTL p. 95
    RDDCOLMOD = const(0x0c)  # Read Display Pixel Format p. 96
    RDDIM = const(0x0d)  # Read Display Image Mode p. 97
    RDDSM = const(0x0e)  # Read Display Signal Mode p. 98
    RDDSDR = const(0x0f)  # Read Display Self-Diagnostic Result p. 99
    SLPIN = const(0x10)  # Enter Sleep Mode p. 100
    SLPOUT = const(0x11)  # Sleep Out p. 101
    PTLON = const(0x12)  # Partial Mode ON p. 103
    NORON = const(0x13)  # Normal Display Mode ON p. 104
    DINVOFF = const(0x20)  # Display Inversion OFF p. 105
    DINVON = const(0x21)  # Display Inversion ON p. 106
    GAMSET = const(0x26)  # Gamma Set p. 107
    DISPOFF = const(0x28)  # Display OFF p. 108
    DISPON = const(0x29)  # Display ON p. 109
    CASET = const(0x2a)  # Column Address Set p. 100
    PASET = const(0x2b)  # Page Address Set p. 112
    RAMWR = const(0x2c)  # Memory Write p. 114
    RGBSET = const(0x2d)  # Color Set p. 115
    RAMRD = const(0x2e)  # Memory Read p. 116
    PTLAR = const(0x30)  # Partial Area p. 118
    VSCRDEF = const(0x33)  # Vertical Scrolling Definition p. 120
    TEOFF = const(0x34)  # Tearing Effect Line OFF p. 124
    TEON = const(0x35)  # Tearing Effect Line ON p. 125
    MADCTL = const(0x36)  # Memory Access Control p. 127
    VSCRSADD = const(0x37)  # Vertical Scrolling Start Address p. 129
    IDMOFF = const(0x38)  # Idle Mode OFF p. 131
    IDMON = const(0x39)  # Idle Mode ON p. 132
    PIXSET = const(0x3a)  # COLMOD: Pixel Format Set p. 134
    WRITE_MEMORY_CONTINUE = const(0x3c)  # Write Memory Continue p. 135
    READ_MEMORY_CONTINUE = const(0x3e)  # Read Memory Continue p. 137
    SET_TEAR_SCANLINE = const(0x44)  # Set Tear Scanline p. 139
    GET_SCANLINE = const(0x45)  # Get Scanline p. 140
    WRDISBV = const(0x51)  # Write Display Brightness p. 141
    RDDISBV = const(0x52)  # Read Display Brightness p. 142
    WRCTRLD = const(0x53)  # Write CTRL Display p. 143
    RDCTRLD = const(0x54)  # Read CTRL Display p. 145
    WRCABC = const(0x55)  # Write Content Adaptive Brightness Control p. 147
    RDCABC = const(0x56)  # Read Content Adaptive Brightness Control p. 148
    WRITE_CABC_MINIMUM_BRIGHTNESS = const(0x5e)  # Write CABC Minimum Brightness, Backlight Control 1 p. 149
    READ_CABC_MINIMUM_BRIGHTNESS = const(0x5f)  # Read CABC Minimum Brightness, Backlight Control 1 p. 150
    RDID1 = const(0xda)  # Read ID1 p. 151
    RDID2 = const(0xdb)  # Read ID2 p. 152
    RDID3 = const(0xdc)  # Read ID2 p. 153
    IFMODE = const(0xb0)  # Interface Mode Control p. 154
    FRMCTR1 = const(0xb1)  # Frame Rate Control (In Normal Mode/Full Colors) p. 155
    FRMCTR2 = const(0xb2)  # Frame Rate Control (In Idle Mode/8 Colors) p. 157
    FRMCTR3 = const(0xb3)  # Frame Rate control (In Partial Mode/Full Colors) p. 159
    INVTR = const(0xb4)  # Display Inversion Control p. 161
    PRCTR = const(0xb5)  # Blanking Porch Control p. 162
    DISCTRL = const(0xb6)  # Display Function Control p. 164
    ETMOD = const(0xb7)  # Entry Mode Set p. 168
    BACKLIGHT_CONTROL_1 = const(0xb8)  # Backlight Control 1 p. 169
    BACKLIGHT_CONTROL_2 = const(0xb9)  # Backlight Control 2 p. 170
    BACKLIGHT_CONTROL_3 = const(0xba)  # Backlight Control 3 p. 172
    BACKLIGHT_CONTROL_4 = const(0xbb)  # Backlight Control 4 p. 173
    BACKLIGHT_CONTROL_5 = const(0xbc)  # Backlight Control 5 p. 175
    BACKLIGHT_CONTROL_7 = const(0xbe)  # Backlight Control 7 p. 176
    BACKLIGHT_CONTROL_8 = const(0xbf)  # Backlight Control 8 p. 177
    PWCTRL1 = const(0xc0)  # Power Control 1 p. 178
    PWCTRL2 = const(0xc1)  # Power Control 2 p. 179
    VMCTRL1 = const(0xc5)  # VCOM Control 1 p. 180
    VMCTRL2 = const(0xc7)  # VCOM Control 2 p. 182
    NVMWR = const(0xd0)  # NV Memory Write p. 184
    NVMPKEY = const(0xd1)  # NV Memory Protection Key p. 185
    RDNVM = const(0xd2)  # NV Memory Status Read p. 186
    RDID4 = const(0xd3)  # Read ID4 p. 187
    PGAMCTRL = const(0xe0)  # Positive Gamma Correction p. 188
    NGAMCTRL = const(0xe1)  # Negative Gamma Correction p. 189
    DGAMCTRL1 = const(0xe2)  # Digital Gamma Control 1 p. 190
    DGAMCTRL2 = const(0xe3)  # Digital Gamma Control 2 p. 191
    IFCTL = const(0xf6)  # Interface Control, 16-bits Data Format Selection p. 192
    POWER_CONTROL_A = const(0xcb)  # Power Control A p. 195
    POWER_CONTROL_B = const(0xcf)  # Power Control B p. 196
    DRIVER_TIMING_CONTROL_A1 = const(0xe8)  # Driver Timing Control A1 p. 197
    DRIVER_TIMING_CONTROL_A2 = const(0xe9)  # Driver Timing Control A2 p. 198
    DRIVER_TIMING_CONTROL_B = const(0xea)  # Driver Timing Control B p. 199
    POWER_ON_SEQUENCE_CONTROL = const(0xed)  # Power On Sequence Control p. 200
    ENABLE_3G = const(0xf2)  # Enable 3G p. 201
    PUMP_RATIO_CONTROL = const(0xf7)  # Pump Ratio Control p. 202
    UNISPACE_FONT = XglcdFont('Unispace12x24.c', 12, 24)  # load font
    POWER_DISPLAY = Pin(2, Pin.OUT)

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
        # initialize GPIO pins and set implementation specific methods
        self.cs.init(self.cs.OUT, value=1)
        self.dc.init(self.dc.OUT, value=0)
        self.rst.init(self.rst.OUT, value=1)
        # send initialization commands
        self.__write_cmd(self.SWRESET)  # software reset
        utime.sleep(.1)
        # init the display
        self.__init_display()

    def __init_display(self):
        """
        Private method to handle init of display
        """
        self.__write_cmd(self.POWER_CONTROL_B, 0x00, 0xC1, 0x30)  # pwr ctrl B
        self.__write_cmd(self.POWER_ON_SEQUENCE_CONTROL, 0x64, 0x03, 0x12, 0x81)  # pwr on seq. ctrl
        self.__write_cmd(self.DRIVER_TIMING_CONTROL_A1, 0x85, 0x00, 0x78)  # driver timing ctrl A
        self.__write_cmd(self.POWER_CONTROL_A, 0x39, 0x2C, 0x00, 0x34, 0x02)  # pwr ctrl A
        self.__write_cmd(self.PUMP_RATIO_CONTROL, 0x20)  # pump ratio control
        self.__write_cmd(self.DRIVER_TIMING_CONTROL_B, 0x00, 0x00)  # driver timing ctrl B
        self.__write_cmd(self.PWCTRL1, 0x23)  # pwr ctrl 1
        self.__write_cmd(self.PWCTRL2, 0x10)  # pwr ctrl 2
        self.__write_cmd(self.VMCTRL1, 0x3E, 0x28)  # VCOM ctrl 1
        self.__write_cmd(self.VMCTRL2, 0x86)  # VCOM ctrl 2
        self.__write_cmd(self.MADCTL, self.rotation)  # mem access ctrl
        self.__write_cmd(self.VSCRSADD, 0x00)  # vertical scrolling start address
        self.__write_cmd(self.PIXSET, 0x55)  # COLMOD: pixel format
        self.__write_cmd(self.FRMCTR1, 0x00, 0x18)  # frame rate ctrl
        self.__write_cmd(self.DISCTRL, 0x08, 0x82, 0x27)
        self.__write_cmd(self.ENABLE_3G, 0x00)  # enable 3 gamma ctrl
        self.__write_cmd(self.GAMSET, 0x01)  # gamma curve selected
        self.__write_cmd(self.PGAMCTRL, 0x0F, 0x31, 0x2B, 0x0C, 0x0E, 0x08, 0x4E, 0xF1, 0x37, 0x07, 0x10, 0x03, 0x0E, 0x09, 0x00)  # noqa
        self.__write_cmd(self.NGAMCTRL, 0x00, 0x0E, 0x14, 0x03, 0x11, 0x07, 0x31, 0xC1, 0x48, 0x08, 0x0F, 0x0C, 0x31, 0x36, 0x0F)  # noqa
        self.__write_cmd(self.SLPOUT)  # exit sleep
        utime.sleep(.1)
        self.__write_cmd(self.DISPON)  # display on
        utime.sleep(.1)
        self.clear()  # display clear

    def __write_cmd(self, command, *args):
        """
        Private method to write command to display

        Params:
            command: bytes
            *args: bytes, optional
        """
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([command]))
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
        self.__write_cmd(self.CASET, *ustruct.pack('>HH', x0, x1))
        self.__write_cmd(self.PASET, *ustruct.pack('>HH', y0, y1))
        self.__write_cmd(self.RAMWR)
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

    def text(self, text, color=0b1111111111100000, font=UNISPACE_FONT, x=8, y=0, background=0, spacing=1,
             sleep_time=3):
        """
        Method to draw text

        Params:
            text: str
            color: int, optional
            font: object, optional
            x: int, optional
            y: int, optional
            background: int, optional
            spacing: int, optional
            sleep_time: int, optional
        """
        self.clear()
        for letter in text:
            if letter == ' ' and x > 144:
                x = 0
                y += 24
            # get letter array and letter dimension
            width, height = self.__letter(letter, color, font, x, y, background)
            x += (width + spacing)
        self.POWER_DISPLAY.value(1)
        utime.sleep(sleep_time)
        self.POWER_DISPLAY.value(0)

    def image(self, path, x=0, y=0, width=240, height=320, draw_speed=1024, sleep_time=2, multithreading=False):
        """
        Method to draw image on display

        Params:
            path: str
            x: int, optional
            y: int, optional
            width: int, optional
            height: int, optional
            draw_speed: int, optional
            sleep_time: int, optional
            multithreading: bool, optional
        """
        if not multithreading:
            self.clear()
        x2 = x + width - 1
        with open(path, 'rb') as f:
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
            utime.sleep(sleep_time)
            self.POWER_DISPLAY.value(0)

    def handle_threading_setup(self):
        """
        Method to handle threading setup functionality to ensure thread does not crash
        """
        self.clear()

    def handle_threading_teardown(self, sleep_time=1):
        """
        Method to handle threading teardown functionality to ensure thread does not crash

        Params:
            sleep_time: int, optional
        """
        self.POWER_DISPLAY.value(1)
        utime.sleep(sleep_time)
        self.POWER_DISPLAY.value(0)
