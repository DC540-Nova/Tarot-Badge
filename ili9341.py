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

from time import sleep
from math import cos, sin, pi, radians
import ustruct
import gc
from micropython import const


def color565(r, g, b):
    """
    Function to return RGB565 color value
    
    Params:
        r: int
        g: int
        b: int
        
    Returns:
        int
    """
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3


class Display():
    """
    Class to handle IL9341 display.
    """

    # ili9341 registers
    NOP = const(0x00)  # no-op
    SWRESET = const(0x01)  # software reset
    RDDID = const(0x04)  # read display ID info
    RDDST = const(0x09)  # read display status
    SLPIN = const(0x10)  # enter sleep mode
    SLPOUT = const(0x11)  # exit sleep mode
    PTLON = const(0x12)  # partial mode on
    NORON = const(0x13)  # normal display mode on
    RDMODE = const(0x0A)  # read display power mode
    RDMADCTL = const(0x0B)  # read display MADCTL
    RDPIXFMT = const(0x0C)  # read display pixel format
    RDIMGFMT = const(0x0D)  # read display image format
    RDSELFDIAG = const(0x0F)  # read display self-diagnostic
    INVOFF = const(0x20)  # display inversion off
    INVON = const(0x21)  # display inversion on
    GAMMASET = const(0x26)  # gamma set
    DISPLAY_OFF = const(0x28)  # display off
    DISPLAY_ON = const(0x29)  # display on
    SET_COLUMN = const(0x2A)  # column address set
    SET_PAGE = const(0x2B)  # page address set
    WRITE_RAM = const(0x2C)  # memory write
    READ_RAM = const(0x2E)  # memory read
    PTLAR = const(0x30)  # partial area
    VSCRDEF = const(0x33)  # vertical scrolling definition
    MADCTL = const(0x36)  # memory access control
    VSCRSADD = const(0x37)  # vertical scrolling start address
    PIXFMT = const(0x3A)  # COLMOD: pixel format set
    WRITE_DISPLAY_BRIGHTNESS = const(0x51)  # brightness hardware dependent
    READ_DISPLAY_BRIGHTNESS = const(0x52)
    WRITE_CTRL_DISPLAY = const(0x53)
    READ_CTRL_DISPLAY = const(0x54)
    WRITE_CABC = const(0x55)  # write content adaptive brightness control
    READ_CABC = const(0x56)  # read content adaptive brightness control
    WRITE_CABC_MINIMUM = const(0x5E)  # write CABC minimum brightness
    READ_CABC_MINIMUM = const(0x5F)  # read CABC minimum brightness
    FRMCTR1 = const(0xB1)  # frame rate control (in normal mode/full colors)
    FRMCTR2 = const(0xB2)  # frame rate control (in idle mode/8 colors)
    FRMCTR3 = const(0xB3)  # frame rate control (in partial mode/full colors)
    INVCTR = const(0xB4)  # display inversion control
    DFUNCTR = const(0xB6)  # display function control
    PWCTR1 = const(0xC0)  # power control 1
    PWCTR2 = const(0xC1)  # power control 2
    PWCTRA = const(0xCB)  # power control Aa
    PWCTRB = const(0xCF)  # power control B
    VMCTR1 = const(0xC5)  # VCOM control 1
    VMCTR2 = const(0xC7)  # VCOM control 2
    RDID1 = const(0xDA)  # read ID 1
    RDID2 = const(0xDB)  # read ID 2
    RDID3 = const(0xDC)  # read ID 3
    RDID4 = const(0xDD)  # read ID 4
    GMCTRP1 = const(0xE0)  # positive gamma correction
    GMCTRN1 = const(0xE1)  # negative gamma correction
    DTCA = const(0xE8)  # driver timing control A
    DTCB = const(0xEA)  # Driver timing control B
    POSC = const(0xED)  # power on sequence control
    ENABLE3G = const(0xF2)  # enable 3 gamma control
    PUMPRC = const(0xF7)  # pump ratio control

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
        self.reset = self.reset_mpy
        self.write_cmd = self.write_cmd_mpy
        self.write_data = self.write_data_mpy
        self.reset()
        # send initialization commands
        self.write_cmd(self.SWRESET)  # software reset
        sleep(.1)
        self.write_cmd(self.PWCTRB, 0x00, 0xC1, 0x30)  # pwr ctrl B
        self.write_cmd(self.POSC, 0x64, 0x03, 0x12, 0x81)  # pwr on seq. ctrl
        self.write_cmd(self.DTCA, 0x85, 0x00, 0x78)  # driver timing ctrl A
        self.write_cmd(self.PWCTRA, 0x39, 0x2C, 0x00, 0x34, 0x02)  # pwr ctrl A
        self.write_cmd(self.PUMPRC, 0x20)  # pump ratio control
        self.write_cmd(self.DTCB, 0x00, 0x00)  # driver timing ctrl B
        self.write_cmd(self.PWCTR1, 0x23)  # pwr ctrl 1
        self.write_cmd(self.PWCTR2, 0x10)  # pwr ctrl 2
        self.write_cmd(self.VMCTR1, 0x3E, 0x28)  # VCOM ctrl 1
        self.write_cmd(self.VMCTR2, 0x86)  # VCOM ctrl 2
        self.write_cmd(self.MADCTL, self.rotation)  # mem access ctrl
        self.write_cmd(self.VSCRSADD, 0x00)  # vertical scrolling start address
        self.write_cmd(self.PIXFMT, 0x55)  # COLMOD: pixel format
        self.write_cmd(self.FRMCTR1, 0x00, 0x18)  # frame rate ctrl
        self.write_cmd(self.DFUNCTR, 0x08, 0x82, 0x27)
        self.write_cmd(self.ENABLE3G, 0x00)  # enable 3 gamma ctrl
        self.write_cmd(self.GAMMASET, 0x01)  # gamma curve selected
        self.write_cmd(self.GMCTRP1, 0x0F, 0x31, 0x2B, 0x0C, 0x0E, 0x08, 0x4E, 0xF1, 0x37, 0x07, 0x10, 0x03, 0x0E, 0x09, 0x00)
        self.write_cmd(self.GMCTRN1, 0x00, 0x0E, 0x14, 0x03, 0x11, 0x07, 0x31, 0xC1, 0x48, 0x08, 0x0F, 0x0C, 0x31, 0x36, 0x0F)
        self.write_cmd(self.SLPOUT)  # exit sleep
        sleep(.1)
        self.write_cmd(self.DISPLAY_ON)  # display on
        sleep(.1)
        self.clear()  # display clear

    def block(self, x0, y0, x1, y1, data):
        """
        Method to write a block of data to display.

        Params:
            x0: int
            y0: int
            x1: int
            y1: int
            data: bytes
        """
        self.write_cmd(self.SET_COLUMN, *ustruct.pack('>HH', x0, x1))
        self.write_cmd(self.SET_PAGE, *ustruct.pack('>HH', y0, y1))
        self.write_cmd(self.WRITE_RAM)
        self.write_data(data)

    def cleanup(self):
        """
        Method to cleanup resources
        """
        self.clear()
        self.display_off()
        self.spi.deinit()

    def clear(self, color=0):
        """
        Method to clear display in 1024 byte blocks

        Params:
            color: int, optional
        """
        w = self.width
        h = self.height
        # clear display in 1024 byte blocks
        if color:
            line = color.to_bytes(2, 'big') * (w * 8)
        else:
            line = bytearray(w * 16)
        for y in range(0, h, 8):
            self.block(0, y, w - 1, y + 7, line)

    def display_off(self):
        """
        Method to turn the display off
        """
        self.write_cmd(self.DISPLAY_OFF)

    def display_on(self):
        """
        Method to turn the display on
        """
        self.write_cmd(self.DISPLAY_ON)

    def draw_circle(self, x0, y0, r, color):
        """
        Method to draw a circle

        Params:
            x0: int
            y0: int
            r: int
            color: int
        """
        f = 1 - r
        dx = 1
        dy = -r - r
        x = 0
        y = r
        self.draw_pixel(x0, y0 + r, color)
        self.draw_pixel(x0, y0 - r, color)
        self.draw_pixel(x0 + r, y0, color)
        self.draw_pixel(x0 - r, y0, color)
        while x < y:
            if f >= 0:
                y -= 1
                dy += 2
                f += dy
            x += 1
            dx += 2
            f += dx
            self.draw_pixel(x0 + x, y0 + y, color)
            self.draw_pixel(x0 - x, y0 + y, color)
            self.draw_pixel(x0 + x, y0 - y, color)
            self.draw_pixel(x0 - x, y0 - y, color)
            self.draw_pixel(x0 + y, y0 + x, color)
            self.draw_pixel(x0 - y, y0 + x, color)
            self.draw_pixel(x0 + y, y0 - x, color)
            self.draw_pixel(x0 - y, y0 - x, color)

    def draw_ellipse(self, x0, y0, a, b, color):
        """
        Method to draw an ellipse

        Params:
            x0: int
            y0: int
            r: int
            color: int
        """
        a2 = a * a
        b2 = b * b
        twoa2 = a2 + a2
        twob2 = b2 + b2
        x = 0
        y = b
        px = 0
        py = twoa2 * y
        # plot initial points
        self.draw_pixel(x0 + x, y0 + y, color)
        self.draw_pixel(x0 - x, y0 + y, color)
        self.draw_pixel(x0 + x, y0 - y, color)
        self.draw_pixel(x0 - x, y0 - y, color)
        # region 1
        p = round(b2 - (a2 * b) + (0.25 * a2))
        while px < py:
            x += 1
            px += twob2
            if p < 0:
                p += b2 + px
            else:
                y -= 1
                py -= twoa2
                p += b2 + px - py
            self.draw_pixel(x0 + x, y0 + y, color)
            self.draw_pixel(x0 - x, y0 + y, color)
            self.draw_pixel(x0 + x, y0 - y, color)
            self.draw_pixel(x0 - x, y0 - y, color)
        # region 2
        p = round(b2 * (x + 0.5) * (x + 0.5) + a2 * (y - 1) * (y - 1) - a2 * b2)
        while y > 0:
            y -= 1
            py -= twoa2
            if p > 0:
                p += a2 - py
            else:
                x += 1
                px += twob2
                p += a2 - py + px
            self.draw_pixel(x0 + x, y0 + y, color)
            self.draw_pixel(x0 - x, y0 + y, color)
            self.draw_pixel(x0 + x, y0 - y, color)
            self.draw_pixel(x0 - x, y0 - y, color)

    def draw_hline(self, x, y, w, color):
        """
        Method to draw a horizontal line

        Params:
            x: int
            y: int
            w: int
            color: int
        """
        if self.is_off_grid(x, y, x + w - 1, y):
            return
        line = color.to_bytes(2, 'big') * w
        self.block(x, y, x + w - 1, y, line)

    def draw_image(self, path, x=0, y=0, w=240, h=320, draw_speed=26375):
        """
        Method to draw image on screen from flash or sd card

        Params:
            path: str
            x: int, optional
            y: int, optional
            w: int, optional
            h: int, optional
            draw_speed: int, optional
        """
        x2 = x + w - 1
        y2 = y + h - 1
        if self.is_off_grid(x, y, x2, y2):
            return
        with open(path, 'rb') as f:
            chunk_height = draw_speed // w  # 153600 total bytes of an image
            chunk_count, remainder = divmod(h, chunk_height)
            chunk_size = chunk_height * w * 2
            chunk_y = y
            if chunk_count:
                for _ in range(0, chunk_count):
                    gc.collect()
                    buf = f.read(chunk_size)
                    self.block(x, chunk_y, x2, chunk_y + chunk_height - 1, buf)
                    chunk_y += chunk_height
            if remainder:
                gc.collect()
                buf = f.read(remainder * w * 2)
                self.block(x, chunk_y, x2, chunk_y + remainder - 1, buf)

    def draw_letter(self, x, y, letter, font, color, background=0, landscape=False):
        """
        Method to draw a single letter as portrait is the default landscape

        Params:
            x: int
            y: int
            letter: str
            font: object
            color: int
            background: int, optional
            landscape: bool, optional
            
        Returns:
            int, int
        """
        buf, w, h = font.get_letter(letter, color, background, landscape)
        # check for errors (Font could be missing specified letter)
        if w == 0:
            return w, h
        if landscape:
            y -= w
            if self.is_off_grid(x, y, x + h - 1, y + w - 1):
                return 0, 0
            self.block(x, y, x + h - 1, y + w - 1, buf)
        else:
            if self.is_off_grid(x, y, x + w - 1, y + h - 1):
                return 0, 0
            self.block(x, y, x + w - 1, y + h - 1, buf)
        return w, h

    def draw_line(self, x1, y1, x2, y2, color):
        """
        Method to draw a line.

        Args:
            x1: int
            y1: int
            x2: int
            y2: int
        """
        # check for horizontal line
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            self.draw_hline(x1, y1, x2 - x1 + 1, color)
            return
        # check for vertical line
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            self.draw_vline(x1, y1, y2 - y1 + 1, color)
            return
        # confirm coordinates in boundary
        if self.is_off_grid(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)):
            return
        # changes in x, y
        dx = x2 - x1
        dy = y2 - y1
        # determine how steep the line is
        is_steep = abs(dy) > abs(dx)
        # rotate line
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        # swap start and end points if necessary
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # recalculate differentials
        dx = x2 - x1
        dy = y2 - y1
        # calculate error
        error = dx >> 1
        ystep = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2 + 1):
            if not is_steep:
                self.draw_pixel(x, y, color)
            else:
                self.draw_pixel(y, x, color)
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx

    def draw_lines(self, coords, color):
        """
        Method to draw multiple lines

        Parmas:
            coords: list
            color: int
        """
        # starting point
        x1, y1 = coords[0]
        # iterate through coordinates
        for i in range(1, len(coords)):
            x2, y2 = coords[i]
            self.draw_line(x1, y1, x2, y2, color)
            x1, y1 = x2, y2

    def draw_pixel(self, x, y, color):
        """
        Method to draw a single pixel

        Args:
            x: int
            y: int
            color: int
        """
        if self.is_off_grid(x, y, x, y):
            return
        self.block(x, y, x, y, color.to_bytes(2, 'big'))

    def draw_polygon(self, sides, x0, y0, r, color, rotate=0):
        """
        Method to draw an n-sided regular polygon

        Params:
            sides: int
            x0: int
            y0: int
            r: int
            color: int
            rotate: float, optional
        """
        coords = []
        theta = radians(rotate)
        n = sides + 1
        for s in range(n):
            t = 2.0 * pi * s / sides + theta
            coords.append([int(r * cos(t) + x0), int(r * sin(t) + y0)])
        # cast to python float first to fix rounding errors
        self.draw_lines(coords, color=color)

    def draw_rectangle(self, x, y, w, h, color):
        """
        Method to draw a rectangle

        Params:
            x: int
            y: int
            w: int
            h: int
            color: int
        """
        x2 = x + w - 1
        y2 = y + h - 1
        self.draw_hline(x, y, w, color)
        self.draw_hline(x, y2, w, color)
        self.draw_vline(x, y, h, color)
        self.draw_vline(x2, y, h, color)

    def draw_sprite(self, buf, x, y, w, h):
        """
        Method to draw a sprite

        Params:
            buf: bytearray
            x: int
            y: int
            w: int
            h: int
        """
        x2 = x + w - 1
        y2 = y + h - 1
        if self.is_off_grid(x, y, x2, y2):
            return
        self.block(x, y, x2, y2, buf)

    def draw_text(self, x, y, text, font, color,  background=0, landscape=False, spacing=1):
        """
        Method to draw text

        Params:
            x: int
            y: int
            text: str
            font: object
            color: int
            background: int, optional
            landscape: bool, optional
            spacing: int, optional
        """
        for letter in text:
            # get letter array and letter dimension
            w, h = self.draw_letter(x, y, letter, font, color, background, landscape)
            # stop on error
            if w == 0 or h == 0:
                print('ivalid width {0} or height {1}'.format(w, h))
                return
            if landscape:
                # fill in spacing
                if spacing:
                    self.fill_hrect(x, y - w - spacing, h, spacing, background)
                # position y for next letter
                y -= (w + spacing)
            else:
                # fill in spacing
                if spacing:
                    self.fill_hrect(x + w, y, spacing, h, background)
                # position x for next letter
                x += (w + spacing)

    def draw_vline(self, x, y, h, color):
        """
        Method to draw a vertical line
        
        Params:
            x: int
            y: int
            h: int
            color: int
        """
        # confirm coordinates in boundary
        if self.is_off_grid(x, y, x, y + h - 1):
            return
        line = color.to_bytes(2, 'big') * h
        self.block(x, y, x, y + h - 1, line)

    def fill_circle(self, x0, y0, r, color):
        """
        Method to filled a circle

        Params:
            x0: int
            y0: int
            r: int
            color: int
        """
        f = 1 - r
        dx = 1
        dy = -r - r
        x = 0
        y = r
        self.draw_vline(x0, y0 - r, 2 * r + 1, color)
        while x < y:
            if f >= 0:
                y -= 1
                dy += 2
                f += dy
            x += 1
            dx += 2
            f += dx
            self.draw_vline(x0 + x, y0 - y, 2 * y + 1, color)
            self.draw_vline(x0 - x, y0 - y, 2 * y + 1, color)
            self.draw_vline(x0 - y, y0 - x, 2 * x + 1, color)
            self.draw_vline(x0 + y, y0 - x, 2 * x + 1, color)

    def fill_ellipse(self, x0, y0, a, b, color):
        """
        Method to fill an ellipse

        Params:
            x0: int
            y0: int
            a: int
            b: int
            color: int
        """
        a2 = a * a
        b2 = b * b
        twoa2 = a2 + a2
        twob2 = b2 + b2
        x = 0
        y = b
        px = 0
        py = twoa2 * y
        # plot initial points
        self.draw_line(x0, y0 - y, x0, y0 + y, color)
        # region 1
        p = round(b2 - (a2 * b) + (0.25 * a2))
        while px < py:
            x += 1
            px += twob2
            if p < 0:
                p += b2 + px
            else:
                y -= 1
                py -= twoa2
                p += b2 + px - py
            self.draw_line(x0 + x, y0 - y, x0 + x, y0 + y, color)
            self.draw_line(x0 - x, y0 - y, x0 - x, y0 + y, color)
        # region 2
        p = round(b2 * (x + 0.5) * (x + 0.5) +
                  a2 * (y - 1) * (y - 1) - a2 * b2)
        while y > 0:
            y -= 1
            py -= twoa2
            if p > 0:
                p += a2 - py
            else:
                x += 1
                px += twob2
                p += a2 - py + px
            self.draw_line(x0 + x, y0 - y, x0 + x, y0 + y, color)
            self.draw_line(x0 - x, y0 - y, x0 - x, y0 + y, color)

    def fill_hrect(self, x, y, w, h, color):
        """
        Method to draw a filled rectangle

        Params:
            x: int
            y: int
            w: int
            h: int
            color: int
        """
        if self.is_off_grid(x, y, x + w - 1, y + h - 1):
            return
        chunk_height = 1024 // w
        chunk_count, remainder = divmod(h, chunk_height)
        chunk_size = chunk_height * w
        chunk_y = y
        if chunk_count:
            buf = color.to_bytes(2, 'big') * chunk_size
            for c in range(0, chunk_count):
                self.block(x, chunk_y,
                           x + w - 1, chunk_y + chunk_height - 1,
                           buf)
                chunk_y += chunk_height
        if remainder:
            buf = color.to_bytes(2, 'big') * remainder * w
            self.block(x, chunk_y,
                       x + w - 1, chunk_y + remainder - 1,
                       buf)

    def fill_rectangle(self, x, y, w, h, color):
        """
        Method to draw a filled rectangle

        Params:
            x: int
            y: int
            w: int
            h: int
            color: int
        """
        if self.is_off_grid(x, y, x + w - 1, y + h - 1):
            return
        if w > h:
            self.fill_hrect(x, y, w, h, color)
        else:
            self.fill_vrect(x, y, w, h, color)

    def fill_polygon(self, sides, x0, y0, r, color, rotate=0):
        """
        Method to draw a filled n-sided regular polygon

        Params:
            sides: int
            x0: int
            y0: int
            r: int
            color: int
            rotate:: int, optional
        """
        # determine side coordinates
        coords = []
        theta = radians(rotate)
        n = sides + 1
        for s in range(n):
            t = 2.0 * pi * s / sides + theta
            coords.append([int(r * cos(t) + x0), int(r * sin(t) + y0)])
        # starting point
        x1, y1 = coords[0]
        # minimum Maximum X dict
        xdict = {y1: [x1, x1]}
        # iterate through coordinates
        for row in coords[1:]:
            x2, y2 = row
            xprev, yprev = x2, y2
            # calculate perimeter
            # check for horizontal side
            if y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 in xdict:
                    xdict[y1] = [min(x1, xdict[y1][0]), max(x2, xdict[y1][1])]
                else:
                    xdict[y1] = [x1, x2]
                x1, y1 = xprev, yprev
                continue
            # non-horizontal side
            # changes in x, y
            dx = x2 - x1
            dy = y2 - y1
            # determine how steep the line is
            is_steep = abs(dy) > abs(dx)
            # rotate line
            if is_steep:
                x1, y1 = y1, x1
                x2, y2 = y2, x2
            # swap start and end points if necessary
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            # recalculate differentials
            dx = x2 - x1
            dy = y2 - y1
            # calculate error
            error = dx >> 1
            ystep = 1 if y1 < y2 else -1
            y = y1
            # calcualte minimum and maximum x values
            for x in range(x1, x2 + 1):
                if is_steep:
                    if x in xdict:
                        xdict[x] = [min(y, xdict[x][0]), max(y, xdict[x][1])]
                    else:
                        xdict[x] = [y, y]
                else:
                    if y in xdict:
                        xdict[y] = [min(x, xdict[y][0]), max(x, xdict[y][1])]
                    else:
                        xdict[y] = [x, x]
                error -= abs(dy)
                if error < 0:
                    y += ystep
                    error += dx
            x1, y1 = xprev, yprev
        # fill polygon
        for y, x in xdict.items():
            self.draw_hline(x[0], y, x[1] - x[0] + 2, color)

    def fill_vrect(self, x, y, w, h, color):
        """
        Method to draw a filled rectangle

        Params:
            x: int
            y: int
            w: int
            h: int
            color: int
        """
        if self.is_off_grid(x, y, x + w - 1, y + h - 1):
            return
        chunk_width = 1024 // h
        chunk_count, remainder = divmod(w, chunk_width)
        chunk_size = chunk_width * h
        chunk_x = x
        if chunk_count:
            buf = color.to_bytes(2, 'big') * chunk_size
            for c in range(0, chunk_count):
                self.block(chunk_x, y,chunk_x + chunk_width - 1, y + h - 1, buf)
                chunk_x += chunk_width
        if remainder:
            buf = color.to_bytes(2, 'big') * remainder * h
            self.block(chunk_x, y, chunk_x + remainder - 1, y + h - 1, buf)

    def is_off_grid(self, xmin, ymin, xmax, ymax):
        """
        Method to check if coordinates extend past display boundaries

        Params:
            xmin: int
            ymin: int
            xmax: int
            ymax: int
        Returns:
            bool
        """
        if xmin < 0:
            print('x-coordinate: {0} below minimum of 0.'.format(xmin))
            return True
        if ymin < 0:
            print('y-coordinate: {0} below minimum of 0.'.format(ymin))
            return True
        if xmax >= self.width:
            print('x-coordinate: {0} above maximum of {1}.'.format(
                xmax, self.width - 1))
            return True
        if ymax >= self.height:
            print('y-coordinate: {0} above maximum of {1}.'.format(
                ymax, self.height - 1))
            return True
        return False

    def load_sprite(self, path, w, h):
        """
        Method to load sprite image

        Params:
            path: str
            w: int
            h: int
        """
        buf_size = w * h * 2
        with open(path, 'rb') as f:
            return f.read(buf_size)

    def reset_mpy(self):
        """
        Method to perform reset, low=initialization, high=normal operation
        """
        self.rst(0)
        sleep(.05)
        self.rst(1)
        sleep(.05)

    def scroll(self, y):
        """
        Method to scroll display vertically

        Params:
            y: int
        """
        self.write_cmd(self.VSCRSADD, y >> 8, y & 0xFF)

    def set_scroll(self, top, bottom):
        """
        Method to set the height of the top and bottom scroll margins

        Params:
            top: int
            bottom: int
        """
        if top + bottom <= self.height:
            middle = self.height - (top + bottom)
            # print(top, middle, bottom)
            self.write_cmd(self.VSCRDEF,
                           top >> 8,
                           top & 0xFF,
                           middle >> 8,
                           middle & 0xFF,
                           bottom >> 8,
                           bottom & 0xFF)

    def write_cmd_mpy(self, command, *args):
        """
        Method to write command to OLED

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
            self.write_data(bytearray(args))

    def write_data_mpy(self, data):
        """
        Method to write data to OLED

        Params:
            data: bytes
        """
        self.dc(1)
        self.cs(0)
        self.spi.write(data)
        self.cs(1)
