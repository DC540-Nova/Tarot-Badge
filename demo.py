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

from ili9341 import Display
from machine import Pin, SPI
from utime import sleep_us, ticks_us, ticks_diff


class BouncingSprite(object):
    """
    Class to handle a bouncing sprite animation
    """

    def __init__(self, path, w, h, screen_width, screen_height, speed, display):
        """
        Params:
            path: str,
            w: int,
            h: int,
            screen_width: int
            screen_height: int
            size: int.
            speed: int
            display: object
        """
        self.buf = display.load_sprite(path, w, h)
        self.w = w
        self.h = h
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.display = display
        self.x_speed = speed
        self.y_speed = speed
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.prev_x = self.x
        self.prev_y = self.y

    def update_pos(self):
        """
        Method to update sprite speed and position
        """
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        x_speed = abs(self.x_speed)
        y_speed = abs(self.y_speed)
        if x + w + x_speed >= self.screen_width:
            self.x_speed = -x_speed
        elif x - x_speed < 0:
            self.x_speed = x_speed
        if y + h + y_speed >= self.screen_height:
            self.y_speed = -y_speed
        elif y - y_speed <= 0:
            self.y_speed = y_speed
        self.prev_x = x
        self.prev_y = y
        self.x = x + self.x_speed
        self.y = y + self.y_speed

    def draw(self):
        """
        Method to draw sprite
        """
        x = self.x
        y = self.y
        prev_x = self.prev_x
        prev_y = self.prev_y
        w = self.w
        h = self.h
        x_speed = abs(self.x_speed)
        y_speed = abs(self.y_speed)
        # determine direction and remove previous portion of sprite
        if prev_x > x:
            # Left
            self.display.fill_vrect(x + w, prev_y, x_speed, h, 0)
        elif prev_x < x:
            # Right
            self.display.fill_vrect(x - x_speed, prev_y, x_speed, h, 0)
        if prev_y > y:
            # Upward
            self.display.fill_vrect(prev_x, y + h, w, y_speed, 0)
        elif prev_y < y:
            # Downward
            self.display.fill_vrect(prev_x, y - y_speed, w, y_speed, 0)
        self.display.draw_sprite(self.buf, x, y, w, h)


def play():
    """
    Function to play demo
    """
    try:
        # Baud rate of 40000000 seems about the max
        spi = SPI(
            0,
            baudrate=40000000,
            sck=Pin(6),
            mosi=Pin(7))
        display = Display(spi, dc=Pin(15), cs=Pin(13), rst=Pin(14))
        display.clear()

        p0 = Pin(0, Pin.OUT)
        p0.value(1)

        # Load sprite
        dc_540_logo = BouncingSprite('dc540_logo.raw', 100, 100, 240, 320, 1, display)

        while True:
            timer = ticks_us()
            dc_540_logo.update_pos()
            dc_540_logo.draw()
            # attempt to set framerate to 30 FPS
            timer_dif = 33333 - ticks_diff(ticks_us(), timer)
            if timer_dif > 0:
                sleep_us(timer_dif)

    except KeyboardInterrupt:
        display.cleanup()  # noqa


play()
