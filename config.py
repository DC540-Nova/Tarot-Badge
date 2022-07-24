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

from machine import Pin, SPI

# button config
BUTTON_LEFT = 21
BUTTON_RIGHT = 22
BUTTON_UP = 19
BUTTON_DOWN = 18
BUTTON_SUBMIT = 17
BUTTON_EXTRA = 16

# display config
display_spi = SPI(0, baudrate=40000000, sck=Pin(6, Pin.OUT), mosi=Pin(7, Pin.OUT))
from ili9341 import Display  # noqa
display = Display(display_spi, dc=Pin(15, Pin.OUT), cs=Pin(13, Pin.OUT), rst=Pin(14, Pin.OUT))

# neo_pixel config
LED_PIN = 5
LED_COUNT = 32
from neo_pixel import NeoPixel  # noqa
neo_pixel = NeoPixel(Pin, LED_PIN, LED_COUNT)

# nrf config
nrf_spi = SPI(1, baudrate=4000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=Pin(10, Pin.OUT),
              mosi=Pin(11, Pin.OUT), miso=Pin(8, Pin.OUT))
from nrf24l01 import NRF  # noqa
nrf = NRF(nrf_spi, csn=Pin(3, Pin.OUT), ce=Pin(0, Pin.OUT))
