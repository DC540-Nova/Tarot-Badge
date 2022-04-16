# MIT License
#
# Designer: Bob German
# Designer: Betsy Lawrie
# Developer: Kevin Thomas
# Developer: Corinne "Rinn" Neidig
#
# Copyright (c) 2021 DC540 Defcon Group
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

import usys
from machine import *

# NeoPixel config
LED_PIN = 5
LED_COUNT = 32
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
BROWN = (165, 42, 42)
ORANGE = (255, 65, 0)
GRAY = (128, 128, 128)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE, BROWN, ORANGE, GRAY)

# Button config
BUTTON_LEFT = Pin(0, Pin.IN, Pin.PULL_UP)
BUTTON_UP = Pin(1, Pin.IN, Pin.PULL_UP)
BUTTON_DOWN = Pin(2, Pin.IN, Pin.PULL_UP)
BUTTON_RIGHT = Pin(3, Pin.IN, Pin.PULL_UP)
BUTTON_SUBMIT = Pin(10, Pin.IN, Pin.PULL_UP)
BUTTON_EXTRA = Pin(8, Pin.IN, Pin.PULL_UP)

# NRF config
if usys.platform == 'rp2':  # Software SPI
    cfg = {'spi': 0, 'copi': 4, 'cipo': 7, 'sck': 6, 'csn': 14, 'ce': 17}
else:
    raise ValueError('Unsupported platform {}'.format(usys.platform))
PIPES = (b'\xe1\xf0\xf0\xf0\xf0', b'\xe1\xf0\xf0\xf0\xf0')