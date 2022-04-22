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

from utime import sleep_us, ticks_us, ticks_diff

from ili9341 import BouncingSprite
from config import *


def play():
    """
    Function to play demo
    """
    dc_540_logo = BouncingSprite('dc540_logo.raw', 115, 115, 240, 320, 1, display)
    display.clear()
    display.POWER_DISPLAY.value(1)
    for _ in range(500):
        timer = ticks_us()
        dc_540_logo.update_pos()
        dc_540_logo.draw()
        # attempt to set framerate to 30 FPS
        timer_dif = 33333 - ticks_diff(ticks_us(), timer)
        if timer_dif > 0:
            sleep_us(timer_dif)
    display.POWER_DISPLAY.value(0)
