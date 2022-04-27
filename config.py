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

# display config
from machine import Pin, SPI
spi = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
from ili9341 import Display  # noqa
display = Display(spi, dc=Pin(15), cs=Pin(13), rst=Pin(14))

# neo_pixel config
LED_PIN = 5
LED_COUNT = 32
from neo_pixel import NeoPixel  # noqa
neo_pixel = NeoPixel(Pin)

# button config
BUTTON_LEFT = Pin(21, Pin.IN, Pin.PULL_UP)
BUTTON_UP = Pin(20, Pin.IN, Pin.PULL_UP)
BUTTON_DOWN = Pin(19, Pin.IN, Pin.PULL_UP)
BUTTON_RIGHT = Pin(18, Pin.IN, Pin.PULL_UP)
BUTTON_SUBMIT = Pin(17, Pin.IN, Pin.PULL_UP)
BUTTON_EXTRA = Pin(16, Pin.IN, Pin.PULL_UP)
import button  # noqa
